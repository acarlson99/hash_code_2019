from collections import namedtuple
import sys

################################################################################

def read_file(path):
    Pic = namedtuple('Pic', ['idx','type','tag_num','tags'])
    lines = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    num_of_pics = int(lines[0][0])
    pics = [line.split() for line in lines[1:]]
    pics = [Pic(idx, pic[0], int(pic[1]), pic[2:]) for idx, pic in enumerate(pics)]
    return (num_of_pics, pics)

"""
def write_file(slides):
    with open(path, 'w') as f:
        f.write(str(len(slides) + '\n'))
        for slide in slides:
            if slide[`]
"""

################################################################################

def main(path):
    num_of_pics, pics = read_file(path)
    print(pics)
    # GUYS! DO STUFF
    #slides = pics # This is just temporary
    #write_file(slides)

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])

