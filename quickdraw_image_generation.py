import os
from PIL import Image, ImageDraw
# binary_file_parser can be found here:
# https://github.com/googlecreativelab/quickdraw-dataset
from binary_file_parser import unpack_drawings

# function to generate JPEG files from QuickDraw binary files
# parameters:
#  - category - QuickDraw category, e.g. 'cat', 'god'
#  - start_index - index of the image in the category package
#  - num_training - number of images for training you ML model
#  - num_testing - number of images for testing your ML model

def generate_images_for_category(category, start_index, num_training, num_testing):
    num_total = num_training + num_testing
    last_index = start_index + num_total
    category_name = category.replace('full-binary-', '').replace('.bin', '')

    os.makedirs('output/training/{}/'.format(category_name))
    os.makedirs('output/testing/{}/'.format(category_name))

    drawings = list(unpack_drawings('raw/' + category))

    for i in range(start_index, start_index+num_total):
        drawing = drawings[i]

        was_recognized = drawing['recognized']
        if was_recognized != 1:
            continue

        img = Image.new('L', size=(255, 255), color=255)
        draw = ImageDraw.Draw(img)

        for stroke in drawing['image']:
            coordinates = []
            for coordinate in zip(stroke[0], stroke[1]):
                coordinate = coordinate[0], coordinate[1]
                coordinates.append(coordinate)
            draw.line(coordinates, fill=(0), width=3)

        file_path = 'output/training/{}/{}.jpeg'.format(category_name, i)
        if i >= num_training + start_index:
            file_path = 'output/testing/{}/{}.jpeg'.format(category_name, i)

        img.save(file_path)

if __name__ == '__main__':
    categories = os.listdir('./raw')
    for category in categories:
        generate_images_for_category(category, 0, 1000, 200)
