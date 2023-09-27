import numpy
from PIL import Image
import shutil
import os

def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    b = []
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        #return image.mode
        channels = 3
        #print(image.mode)
    elif image.mode == "RGBA":
        #return image.mode
        b.append(image_path)
        ch = '29.3.22/orig/'
        for ele in b:
            res = ele.replace(ch, '') 
        ls.append(res)
        #print(image.mode)
    else:
        #print("Unknown mode: %s" % image.mode)
        pass


"""
t1 = ['org_bus_logo1616808006.9434.png','org_bus_logo1616807248.8887.png','org_bus_logo1616814784.308.png']
ls = []
for i in t1:
    image = get_image(f'29.3.22/orig/{i}')
print(b)
"""

h1 = '29.3.22/orig/' 
s1 = os.listdir(h1)
h2 = '29.3.22/tr/'
s2 = os.listdir(h2)
h1new = '29.3.22/ntr'

ls = []

for i in s1:
    name = f'{i}'
    source = get_image(f'29.3.22/orig/{name}')
print(ls)

print("RGBA separated")

for i in ls:
    name = f'{i}'s
    source = f'29.3.22/orig/{name}'
    dest = f'29.3.22/ntr/{name}'
    task = shutil.copyfile(source, dest)
print("file moved")


