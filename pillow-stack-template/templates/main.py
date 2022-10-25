from PIL import Image, ImageFilter

from pillow_utils import convert_jpg_to_png, create_thumbnail, flip_image, apply_filter, merge_images

if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    # Images used in the tests
    image = Image.open('img_input//gru.jpg')
    image_2 = Image.open('img_input//minions.jpg')

    # Tests
    convert_jpg_to_png(image)

    create_thumbnail(image)

    flip_image(image)

    # Get other possible filters in the ImageFilter class documentation
    apply_filter(image, ImageFilter.BLUR)

    merge_images(image, image_2)