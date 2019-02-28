import numpy as np
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

def score(p1, p2):
    s1 = len(list(set(p1[3]).intersection(p2[3])))
    s2 = len(np.setdiff1d(p1[3], p2[3]))
    s3 = len(np.setdiff1d(p2[3], p1[3]))
    return (min(s1, s2, s3))

def main(path):
    num_of_pics, pics = read_file(path)
    print(num_of_pics, pics)
    print(pics)
    # GUYS! DO STUFF
    #slides = pics # This is just temporary
    #write_file(slides)

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])

