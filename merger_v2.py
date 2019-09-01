import os, sys
from PIL import Image
from math import ceil

'''
merger_v2.py mode src_path saved_name
mode:
    l: linear
    w: wrap
    v: vertical
    h: horizontal
src_path: directory or images
saved_name: saved name with subname
'''

def Merging(mode, src_path, saved):
    width, height = 0, 0
    x_offset, y_offset = 0, 0
    x, y = 0, 0

    images = appendFile(src_path)
    n_imgs = len(images)

    # Resizeing
    for i in images:
        width += i.width
        height += i.height

    width //= n_imgs
    height //= n_imgs
    print('[.]Images resize to {} x {}'.format(width, height))

    for i in range(len(images)):
        images[i] = images[i].resize((width, height))

    # Selecting mode
    if mode == 'hl':
        print('[.]Mode: Horizontal, Linear')
        x = n_imgs
        y = 1

    elif mode == 'hw':
        print('[.]Mode: Horizontal, Wrap')
        x = ceil(n_imgs / 2)
        y = ceil(n_imgs / x)

    elif mode == 'lv':
        print('[.]Mode: Vertical, Linear')
        x = 1
        y = n_imgs

    elif mode == 'vw':
        print('[.]Mode: Vertical, Wrap')
        y = ceil(n_imgs / 2)
        x = ceil(n_imgs / y)

    else:
        print('[!]Unknow mode')
        exit()

    # Final windth, height
    width = images[0].width * x
    height = images[0].height * y

    print('[.]x: {}, y: {}'.format(x, y))

    # Create image template
    template_img = Image.new('RGB', (width, height), color=0xffffff)
    cnt = 0
    for i in range(x):
        for j in range(y):
            template_img.paste(images[cnt], (x_offset + images[0].width * i, y_offset + images[0].height * j))
            print('[.]Image{} pasted'.format(cnt))

            cnt += 1
            if cnt >= n_imgs:
                break

    template_img.save(saved, 'JPEG', quality=80, optimize=True, Progressive=True)
    print('[+]Image saved to {}'.format(os.path.abspath(saved)))

def appendFile(src_path):

    if os.path.isdir(src_path[0]):
        root_path = os.path.abspath(src_path[0])
        src_path = os.listdir(src_path[0])
        src_path = [os.path.join(root_path, src) for src in src_path]

    print('[.]Images to merge:\n[.]    {}'.format('\n[.]    '.join(src_path)))
    images = []
    for img in src_path:
        if img.split('.')[-1].lower() in ['jpg', 'jpeg', 'png']:
            images.append(Image.open(img))
        else:
            print('[-]{} might not be a image. Check carefully!'.format(img))

    return images

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 4:
        print('[!]Missing arguments. Check yourself!')
        exit()

    mode = args[1]
    mode = ''.join(sorted(mode))
    src_path = args[2:-1]
    saved_name = args[-1]

    Merging(mode, src_path, saved_name)