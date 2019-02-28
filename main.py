import sys

################################################################################

def read_file(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    num_of_pics = int(lines[0][0])
    pics = [line.split() for line in lines[1:]]
    pics = [(idx, pic[0], int(pic[1]), pic[2:]) for idx, pic in enumerate(pics)]
    return (num_of_pics, pics)

################################################################################

def main(path):
    num_of_pics, pics = read_file(path)
    print(num_of_pics, pics)

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        main(sys.argv[1])

