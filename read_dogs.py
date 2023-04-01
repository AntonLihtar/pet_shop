import os


def return_list(path: str) -> list:
    pets = []
    for name_dir in os.listdir(path):
        text_content = ''
        dogs_img = ''
        for name_file in os.listdir(f'{path}/{name_dir}'):
            if name_file.split('.')[1] == 'txt':
                with open(f'{path}/{name_dir}/{name_file}') as f:
                    text_content = f.read()

            if name_file.split('.')[1] == 'jpg':
                dogs_img = f'{path}/{name_dir}/{name_file}'

        pets.append({'name': name_dir, 'img': dogs_img, 'text': text_content})
    return pets


def return_dict(path: str) -> dict:
    title_list = path.split('/')[-1]
    return {'title': title_list, 'pets': return_list(path)}


DOGS = return_dict('static/content/dogs')
CATS = return_dict('static/content/cats')
FISH = return_dict('static/content/fish')

print(DOGS)
