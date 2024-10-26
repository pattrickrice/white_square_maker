import argparse
from PIL import Image
from os import listdir
from os.path import isfile, join
from structlog import get_logger

log = get_logger()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=str, help="directory to convert")
    args = parser.parse_args()
    path = args.directory
    files = get_files(path)
    for file in files:
        source = join(path, file)
        out = join(path, file.split(".")[0] + "-white." + file.split(".")[1])
        square_image(source, out)


def get_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def square_image(image_path, output_path):
    """Squares an image by adding white background."""
    log.info("processing", image_path=image_path, output_path=output_path)
    # Open the image
    img = Image.open(image_path)

    # Get the width and height of the image
    width, height = img.size

    # Calculate the size of the square
    size = max(width, height)

    # Create a new image with a white background
    new_img = Image.new("RGB", (size, size), "white")

    # Paste the original image onto the new image, centered
    x_offset = (size - width) // 2
    y_offset = (size - height) // 2
    new_img.paste(img, (x_offset, y_offset))

    # Save the squared image
    new_img.save(output_path)


if __name__ == "__main__":
    main()
