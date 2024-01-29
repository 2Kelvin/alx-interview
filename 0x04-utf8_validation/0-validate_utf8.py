#!/usr/bin/python3
'''utf-8 validation'''


def validUTF8(data):
    '''Checks if the data is a valid utf-8 encoding'''
    leadBytes = 0
    bitPattern1 = 1 << 7
    bitPattern2 = 1 << 6
    for eachByte in data:
        mBytes = 1 << 7
        if leadBytes == 0:
            while mBytes & eachByte:
                leadBytes += 1
                mBytes = mBytes >> 1
            if leadBytes == 0:
                continue
            if leadBytes == 1 or leadBytes > 4:
                return False
        else:
            if not (eachByte & bitPattern1 and not (eachByte & bitPattern2)):
                return False
        leadBytes -= 1
    if leadBytes == 0:
        return True
    else:
        return False
