import exifread


def GetImageDate(fpath):
    f = open(fpath, 'rb')
    try:
        tags = exifread.process_file(f, strict=True)
    except ValueError:
        f.close()
        return False
    f.close()
    # print(fpath)
    # print(str(tags['EXIF DateTimeDigitized'])+'='+str(tags['EXIF DateTimeOriginal']) + '=' + str(tags['Image DateTime']))
    if len(tags) == 0:
        return False
    try:
        return str(tags['EXIF DateTimeOriginal'])
    except:
        try:
            return str(tags['Image DateTime'])
        except:
            try:
                return str(tags['EXIF DateTimeDigitized'])
            except:
                return False
