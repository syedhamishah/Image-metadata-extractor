from PIL import Image
import exifread
import os

def extract_metadata(image_path):
    # Ensure the file exists
    if not os.path.isfile(image_path):
        print("Error: File not found.")
        return

    try:
        # Extract EXIF data
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)

        print("\n--- Image Metadata ---")
        # Filter for key tags of interest
        key_tags = ['Image Make', 'Image Model', 'EXIF DateTimeOriginal', 'EXIF ExposureTime', 'EXIF FNumber', 'EXIF ISOSpeedRatings']
        for tag in key_tags:
            if tag in tags:
                print(f"{tag}: {tags[tag]}")

        # Additional image properties
        with Image.open(image_path) as img:
            print("\n--- Image Properties ---")
            print(f"Image Format: {img.format}")
            print(f"Image Size: {img.size} (Width x Height)")
            print(f"Image Mode: {img.mode}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    image_path = input("Please enter the path to the image file: ")
    extract_metadata(image_path)

if __name__ == "__main__":
    main()
