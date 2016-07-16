from hashlib import sha256


def GetSha256(fpath):
    f = open(fpath, 'rb')
    content = f.read()
    f.close()
    try:
        return sha256(content).hexdigest()
    except:
        return False
