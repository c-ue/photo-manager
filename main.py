import os
import sys

import photo


def main(path=sys.argv[1], tar_dir=sys.argv[2]):
    file_list = []
    tree = list(os.walk(path))
    for i in tree:
        if len(i[2]) == 0:
            continue
        for j in i[2]:
            file = os.path.join(i[0], j)
            info = photo.GetImage(file)
            if info['sha256'] not in [x['sha256'] for x in file_list]:
                file_list.append(info)
    print('Merge index created.\nTotal %d files.' % (len(file_list),))
    print('Start to copy')
    if not os.path.isdir(tar_dir):
        os.makedirs(tar_dir)
    for i in range(len(file_list)):
        print('[*]complete percent:%10.8s%s' % (str(i / len(file_list) * 100), '%'), end='\r')
        photo.MergeImage(tar_dir, file_list[i])
    print('[OK]completed...' + ' ' * 100, end='')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('python3 main.py [files_path] [target_path]')
        sys.exit()
    main()
