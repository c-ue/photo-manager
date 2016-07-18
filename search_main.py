import hashlib
import os
import sys


def main(path=sys.argv[1]):
    index = {}
    file_list = list(os.walk(path))
    for i in file_list:
        for j in i[2]:
            dig = sha(os.path.join(i[0], j))
            if dig in index:
                index[dig].append(os.path.join(i[0], j))
            else:
                index[dig] = [os.path.join(i[0], j)]
    print('Index build completed.')
    while True:
        file = input('File(quit to exit):').strip('"')
        if file.upper() == 'QUIT':
            sys.exit()
        if file == '':
            continue
        try:
            dig = sha(file)
        except:
            print('No such file or directory')
            continue
        print('total %d file:' % (len(index[dig]),))
        for i in index[dig]:
            print(i)


def sha(file):
    f = open(file, 'rb')
    hex = hashlib.sha256(f.read()).hexdigest()
    f.close()
    return hex


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('python main.py  [path]')
        sys.exit()
    main()
