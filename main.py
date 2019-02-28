#!/usr/bin/env python3

import os
import numpy as np
from collections import namedtuple
import sys

################################################################################

Pic = namedtuple('Pic', ['idx','type','tag_num','tags'])

def read_file(path):
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
        f.write(str(len(slides)) + '\n')
        idx = 0
        while idx < len(slides):
            if len(slides[idx]) == 1 and slides[idx][0].type == 'H':
                f.write(str(slides[idx][0].idx) + '\n')
            elif len(slides[idx]) == 2:
                f.write(str(slides[idx][0].idx) + ' ' + str(slides[idx][1].idx) + '\n')
            idx += 1

################################################################################

def pair_vpics(pics):
    """
    Number of vertical pics must be even for this to work.
    """
    lst = []
    idx = 0
    while idx < len(pics)-1:
        if pics[idx].type == 'V' and pics[idx+1].type != 'V':
            tmp = []
            tmp.append(Pic(pics[idx].idx, pics[idx].type, pics[idx].tag_num,
                        list(pics[idx].tags)))
            jdx = idx+1
            while jdx < len(pics):
                if (pics[jdx].type == 'V'):
                    tmp.append(Pic(pics[jdx].idx, pics[jdx].type, pics[jdx].tag_num,
                        list(pics[jdx].tags)))
                    pics[jdx] = Pic(0,0,0,0)
                    break
                jdx += 1
            lst.append(tmp)
            idx += 1
        elif pics[idx].type == 'V' and pics[idx+1].type == 'V':
            tmp = []
            tmp.append(Pic(pics[idx].idx, pics[idx].type, pics[idx].tag_num,
                        list(pics[idx].tags)))
            tmp.append(Pic(pics[idx+1].idx, pics[idx+1].type, pics[idx+1].tag_num,
                        list(pics[idx+1].tags)))
            lst.append(tmp)
            idx += 1
        elif pics[idx].type == 'H' or pics[idx].type == 'V':
            lst.append([pics[idx]])
        idx += 1
    lst.append([pics[-1]])
    return lst

def pair_again(slides):
    lst = []
    idx = 0;
    len_ = len(slides)
    while idx < len_:
        if slides[idx].type == 'H':
            lst.append([slides[idx]])
            idx += 1
        elif slides[idx].type == 'V':
            lst.append([slides[idx], slides[idx+1]])
            idx += 2
            #len_ -= 1
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
    hpics = list(filter(lambda p: p.type == 'H', pics))
    vpics = list(filter(lambda p: p.type == 'V', pics))
    with open("the_answer.txt", 'w') as f:
        f.write(str(int(len(hpics) + len(vpics) / 2)) + "\n")
        for n in hpics:
            f.write(str(n.idx) + "\n")
        i = 0
        while i < len(vpics) - 1:
            f.write(str(vpics[i].idx) + " " + str(vpics[i+1].idx) + "\n")
            i += 2
#    sort(pics)
    # GUYS! DO STUFF
    # slides = pics
#    print(pics)
    # slides = pair_vpics(pics) # This is just temporary
#    slides = pair_again(slides)
    # slides = list(filter(lambda s: s != Pic(0,0,0,0), slides))
    # write_file('the_answer.txt', slides)

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])

