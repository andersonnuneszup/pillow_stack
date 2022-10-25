# All the references in https://pillow.readthedocs.io/en/stable/reference/
from PIL import Image


def convert_jpg_to_png(img):
    img.save('img_output/img_converted.png')


def create_thumbnail(img):
    img.thumbnail((200, 200))
    img.save('img_output/img_thumbnail.jpg')


def flip_image(img):
    img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save('img_output/img_flip.jpg')


def rotate_image_90_degrees(img):
    img.rotate(90)
    img.save('img_output/img_rotated.jpg')


def crop_image(img, left, upper, right, lower):
    img.crop(left, upper, right, lower)
    img.save('img_output/img_cropped.jpg')


def convert_image_to_grayscale(img):
    grayscale_img = img.convert('L')
    grayscale_img.save('img_output/img_grayscale.jpg')


def apply_filter(img, filter):
    filtered_img = img.filter(filter)
    filtered_img.save('img_output/img_filtered.jpg')


def resize_img(img, width, height):
    img_resized = img.resize((width, height))
    img_resized.save('img_output/img_resized.jpg')


def merge_images(img_1, img_2):
    w = img_1.size[0] + img_2.size[0]
    h = max(img_1.size[1], img_2.size[1])
    merged_img = Image.new("RGB", (w, h))

    merged_img.paste(img_1)
    merged_img.paste(img_2, (img_1.size[0], 0))

    merged_img.save('img_output/merged_img.jpg')