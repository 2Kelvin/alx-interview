#!/usr/bin/python3
'''Log parsing'''
import sys

dictCodes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

tSize = 0
count = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            scode = line_list[-2]
            fSize = int(line_list[-1])
            if scode in dictCodes.keys():
                dictCodes[scode] += 1
            tSize += fSize
            count += 1
        if count == 10:
            count = 0
            print('File size: {}'.format(tSize))
            for x, y in sorted(dictCodes.items()):
                if y != 0:
                    print('{}: {}'.format(x, y))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(tSize))
    for x, y in sorted(dictCodes.items()):
        if y != 0:
            print('{}: {}'.format(x, y))