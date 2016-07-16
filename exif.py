import exifread


def GetImageDate(fpath):
    f = open(fpath, 'rb')
    tags = exifread.process_file(f, strict=True)
    f.close()
    # print(fpath)
    # print(str(tags['EXIF DateTimeDigitized'])+'='+str(tags['EXIF DateTimeOriginal']) + '=' + str(tags['Image DateTime']))
    if len(tags) == 0:
        return False
    return str(tags['EXIF DateTimeOriginal'])
