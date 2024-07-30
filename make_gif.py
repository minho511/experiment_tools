import os
from PIL import Image
from IPython.display import Image as Img
from IPython.display import display

frames_path = ""
output_path = ""
file_name = ""
def generate_gif(path, idx):
    img_list = os.listdir(path)
    img_list = [path + '/' + x for x in img_list]
    images = [Image.open(x) for x in img_list]
    
    im = images[0]
    im.save(f'output_path/{file_name}.gif', save_all=True, append_images=images[1:],loop=0xff, duration=500)
    return Img(url='output_path/{file_name}.gif')

gif = generate_gif(frames_path)
display(gif)

