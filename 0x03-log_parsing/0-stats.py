#!/usr/bin/python3
"""
Log parsing module.
To add robust checking using regular expression
"""

import sys
import signal


lineNumber = 0
currentStats = {}
fileSize = 0


def printstats(sig=0, frame=0):
    """print stats
    """
    print("File size: {}".format(fileSize))
    for key in sorted(currentStats):
        print("{}: {}".format(key, currentStats[key]))


signal.signal(signal.SIGINT, printstats)

for line in sys.stdin:
    try:
        a = line.split(" ")
        code = float(a[-2])
        if (code in [200, 301, 400, 401, 403, 404, 405, 500]):
            code = int(code)
        else:
            continue
        cond1 = (len(a) == 9)
        number = int(a[-1])
        cond2 = (a[-3] == 'HTTP/1.1"')
        cond3 = (a[-4] == '/projects/260')
        cond4 = (a[-5] == '"GET')
        if (cond1 and cond2 and cond3 and cond4):
            currentStats[code] = currentStats.get(code, 0) + 1
            fileSize += number
            lineNumber += 1
        if lineNumber % 10 == 0:
            printstats()
            continue
    except Exception as e:
        continue
