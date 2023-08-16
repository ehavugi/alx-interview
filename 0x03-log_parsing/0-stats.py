#!/usr/bin/python3
"""
Log parsing module.
To add robust checking using regular expression.

"""
import re

lineNumber = 0
currentStats = {}
fileSize = 0
while True:
    line = input()
    a = line.split(" ")
    lineNumber += 1
    try:
        code = int(a[-2])
        assert(code in [200, 301, 400, 401, 403, 404, 405, 500])
        number = int(a[-1])
        assert(a[-3] == 'HTTP/1.1"')
        assert(a[-4] == '/projects/260')
        assert(a[-5] == '"GET')
        currentStats[code] = currentStats.get(code, 0) + 1
        fileSize += number
    except Exception as e:
        lineNumber -= 1
        # print("failed", e)
        # print(a[-1], a[-2])
    if lineNumber % 10 == 0:
        print("File size: {}".format(fileSize))
        for key in sorted(currentStats):
            print("{}: {}".format(key, currentStats[key]))
