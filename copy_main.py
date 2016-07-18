import os
import shutil
import sys

try:
    def main(src_dir=sys.argv[1], dst_dir=sys.argv[2]):
        dst_list = list(os.walk(dst_dir))
        src_list = list(os.walk(src_dir))
        fst = len(dst_list[0][2]) + 1
        print('first photo is %d' % (fst,), end='\t')
        for i in src_list[0][2]:
            shutil.copy2(os.path.join(src_list[0][0], i),
                         os.path.join(dst_list[0][0], str(fst) + '.' + i.split('.')[-1]))
            fst += 1
        print('last photo is %d' % (fst - 1,))
except:
    pass

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('python copy_main.py [src-dir] [dst-dir]')
        sys.exit()
    main()
