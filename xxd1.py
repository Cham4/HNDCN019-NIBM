import os.path
import string
import sys


def print_buf(countr, buf):
    buf2 = [('%02x' % ord(i)) for i in buf]
    print '{0}: {1:<39}  {2}'.format(('%07x' % (countr * 16)),
        ' '.join([''.join(buf2[i:i + 2]) for i in range(0, len(buf2), 2)]),
        ''.join([c if c in string.printable[:-5] else '.' for c in buf]))


def process_xxd(file_path):
    with open(file_path, 'r') as f:
        countr = 0
        while True:
            buf = f.read(16)
            if not buf:
                break
            print_buf(countr, buf)
            countr += 1


if __name__ == '__main__':
    if not os.path.exists(sys.argv[1]):
        print >> (sys.stderr, "The file doesn't exist.")
        sys.exit(1)
    process_xxd(sys.argv[1])
