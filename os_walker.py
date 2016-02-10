#!/usr/bin/python
__author__ = "daVinci13"

import os

let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in let:
    try:
        rootdir = i + ":\\" #if used on Mac or Linux, rootdir = "\"
        for curr, dirs, files in os.walk(rootdir):
            for f in files:
                if f.endswith("pdf"): #replace pdf with file type You are looking for
                    print ('%s/%s' % (curr, f))
                else:
                    pass
    except Exception as e:
        print rootdir, "does not exist.", e
