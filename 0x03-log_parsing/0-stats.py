#!/usr/bin/python3
"""
Log parsing module.
To add robust checking using regular expression.
"""
import sys


lineNumber = 0
currentStats = {}
fileSize = 0
for line in sys.stdin:
    try:
        a = line.split(" ")
        try:
            code = float(a[-2])
            assert(code in [200, 301, 400, 401, 403, 404, 405, 500])
            code = int(code)
            assert(len(a) == 9)
            number = int(a[-1])
            assert(a[-3] == 'HTTP/1.1"')
            assert(a[-4] == '/projects/260')
            assert(a[-5] == '"GET')
            currentStats[code] = currentStats.get(code, 0) + 1
            fileSize += number
            lineNumber += 1
        except KeyboardInterrupt:
            print("File size: {}".format(fileSize))
            for key in sorted(currentStats):
                print("{}: {}".format(key, currentStats[key]))
            break
        except Exception as e:
            if e == KeyboardInterrupt:
                pass
        if lineNumber % 10 == 0:
            print("File size: {}".format(fileSize))
            for key in sorted(currentStats):
                print("{}: {}".format(key, currentStats[key]))
    except KeyboardInterrupt:
        print("File size: {}".format(fileSize))
        for key in sorted(currentStats):
            print("{}: {}".format(key, currentStats[key]))
