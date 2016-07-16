import os
import shutil
import time

import exif
import hash


def GetImage(fpath):
    date = exif.GetImageDate(fpath)
    if date == False:
        print('%s is not a photo.' % (fpath,))
        date = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.stat(fpath).st_mtime))
    dig = hash.GetSha256(fpath)
    if dig == False:
        print('hash %s error.\n' % (fpath,))
        return False
    fname = fpath.split('\\')[-1]
    fileinfo = {'name': fname, 'sha256': dig, 'date': date, 'path': fpath}
    return fileinfo


def MergeImage(tar_dir, fileinfo):
    folder = fileinfo['date'].split(':')[0] + '-' + fileinfo['date'].split(':')[1] + '-' + \
             fileinfo['date'].split(':')[2].split(' ')[0]
    dir = os.path.join(tar_dir, folder)
    if not os.path.isdir(dir):
        os.makedirs(dir)
    fname = str(len(list(os.walk(dir))[0][2]) + 1)
    shutil.copy2(fileinfo['path'], os.path.join(dir, fname + '.' + fileinfo['path'].split('.')[-1]))
