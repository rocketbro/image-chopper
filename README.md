# Image Chopper

Image Chopper is a Python script that automatically chops tall images into smaller sections. It's particularly useful for processing large vertical images that need to be split into more manageable sizes.

## Features

- Chops images taller than a specified height into multiple sections
- Supports various image formats (PNG, JPG, JPEG, GIF, BMP)
- Customizable maximum height for chopped sections
- Skips non-image files and provides informative console output
- Easy to use with command-line arguments

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone this repository or download the `image_chopper.py` file.
2. Install the required Pillow library:
pip install Pillow
Copy
## Usage

Run the script from the command line with the following syntax:
python image_chopper.py <input_directory> <output_directory> [-maxheight MAX_HEIGHT]
Copy
- `<input_directory>`: Path to the directory containing the images you want to process
- `<output_directory>`: Path to the directory where the chopped images will be saved
- `-maxheight MAX_HEIGHT`: (Optional) Maximum height for each chopped section (default is 4096 pixels)

### Examples

1. Using default settings:
python image_chopper.py /path/to/input/images /path/to/output/images
Copy
2. Specifying a custom max height:
python image_chopper.py /path/to/input/images /path/to/output/images -maxheight 2000
Copy
## How It Works

1. The script scans the input directory for image files.
2. For each image taller than the specified max height:
- It calculates how many sections the image needs to be divided into.
- It crops the image into sections, each no taller than the max height.
- The sections are saved in the output directory with names like `original_filename_part1.jpg`, `original_filename_part2.jpg`, etc.
3. Images not exceeding the max height are skipped.
4. Non-image files are ignored.

## Notes

- The script will create the output directory if it doesn't exist.
- Hidden files (like `.DS_Store` on macOS) are automatically skipped.
- The original images in the input directory are not modified.