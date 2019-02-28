#!/usr/bin/env python3

import os
import numpy as np
from collections import namedtuple
import sys

################################################################################

def read_file(path):
    Pic = namedtuple('Pic', ['idx','type','tag_num','tags'])
    lines = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    num_of_pics = int(lines[0])
    pics = [line.split() for line in lines[1:]]
    pics = [Pic(idx, pic[0], int(pic[1]), pic[2:]) for idx, pic in enumerate(pics)]
    return (num_of_pics, pics)

def write_file(path, slides):
    """
    Vertical slices must be together; otherwise, this does not work!!!
    """
    with open(path, 'w') as f:
        f.write(str(len(slides)-1) + '\n')
        idx = 0
        while idx < len(slides):
            if slides[idx].type == 'H':
                f.write(str(slides[idx].idx) + '\n')
            elif slides[idx].type == 'V':
                f.write(str(slides[idx].idx) + ' ')
                if idx+1 < len(slides):
                    f.write(str(slides[idx+1].idx) + '\n')
                idx += 1
            idx += 1

################################################################################

def pair_vpics(pics):
    """
    Number of vertical pics must be even for this to work.
    """
    Pic = namedtuple('Pic', ['idx','type','tag_num','tags'])
    lst = []
    idx = 0
    while idx < len(pics)-1:
        if pics[idx].type == 'V' and pics[idx+1].type != 'V':
            lst.append(pics[idx])
            jdx = idx+1
            while jdx < len(pics):
                if (pics[jdx].type == 'V'):
                    lst.append(Pic(pics[jdx]))
                    pics[jdx] = Pic(0,0,0,0)
                    break
                jdx += 1
            idx += 1
        elif pics[idx].type == 'H' or pics[idx].type == 'V':
            lst.append(pics[idx])
        idx += 1
    return lst

################################################################################

def score(p1, p2):
    s1 = len(list(set(p1.tags).intersection(p2.tags)))
    s2 = len(np.setdiff1d(p1.tags, p2.tags))
    s3 = len(np.setdiff1d(p2.tags, p1.tags))
    return (min(s1, s2, s3))

def sort(pics):
    go = 1
    while go:
        go = 0
        for i in range(len(pics)):
            try:
                if (score(pics[i], pics[i+1]) > score(pics[i], pics[i+2])):
                    go = 1
                    tmp = pics[i]
                    pics[i] = pics[i+1]
                    pics[i+1] = tmp
            except IndexError:
                break
    return (pics)

def main(path):
    num_of_pics, pics = read_file(path)
#    sort(pics)
    # GUYS! DO STUFF
    slides = pics
    slides = pair_vpics(pics) # This is just temporary
    write_file('the_answer.txt', slides)

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])

