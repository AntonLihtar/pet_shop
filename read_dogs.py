import os
from pprint import pprint


DOGS ={}
path1 = 'static/content/dogs'


for name_dir in os.listdir(path1):
    text_content = ''
    dogs_img = ''
    for name_file in os.listdir(f'{path1}/{name_dir}'):
        if name_file.split('.')[1] == 'txt':
            with open(f'{path1}/{name_dir}/{name_file}') as f:
                text_content = f.read()

        if name_file.split('.')[1] == 'jpg':
            dogs_img = f'{path1}/{name_dir}/{name_file}'

    DOGS[name_dir] = [dogs_img, text_content]


pprint(DOGS)






# with open(path1, 'r') as f:
#     res1 = f.read()
#     print(res1)