import os
import sys
import argparse
from PIL import Image

def chop_images(input_dir, output_dir, max_height=4096):
    """
    Chops tall images in the input directory into sections no taller than the max height.
    Only images that need to be chopped are saved in the output directory.
    
    Parameters:
    input_dir (str): Path to the directory containing the tall images
    output_dir (str): Path to the directory where the chopped images will be saved
    max_height (int): Maximum height for each chopped image section (default is 4096)
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(input_dir, filename)
            try:
                with Image.open(image_path) as image:
                    width, height = image.size
                    
                    if height > max_height:
                        sections = height // max_height
                        if height % max_height > 0:
                            sections += 1
                        
                        for i in range(sections):
                            top = i * max_height
                            bottom = min((i + 1) * max_height, height)
                            cropped = image.crop((0, top, width, bottom))
                            
                            output_filename = f"{os.path.splitext(filename)[0]}_part{i+1}{os.path.splitext(filename)[1]}"
                            output_path = os.path.join(output_dir, output_filename)
                            cropped.save(output_path)
                        print(f"Chopped {filename} into {sections} parts.")
                    else:
                        print(f"Skipping {filename}: Height is not greater than {max_height}.")
            except (IOError, OSError, Image.UnidentifiedImageError):
                print(f"Skipping file {filename}: Not a valid image or unable to process.")
                continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chop tall images into smaller sections.")
    parser.add_argument("input_dir", help="Path to the directory containing the tall images")
    parser.add_argument("output_dir", help="Path to the directory where the chopped images will be saved")
    parser.add_argument("-maxheight", type=int, default=4096, help="Maximum height for each chopped image section (default: 4096)")
    
    args = parser.parse_args()
    
    chop_images(args.input_dir, args.output_dir, args.maxheight)
    print(f"Image processing complete. Chopped images saved in {args.output_dir}")