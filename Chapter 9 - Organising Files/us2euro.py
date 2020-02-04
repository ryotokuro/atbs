#! python3

#us2euro

import re, os, shutil

# 1. Create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?)  # catch any text before the date if any
                        ((0|1)?\d)-  # the month (one/two digits ranging from 01 to 12)
                        ((0|1|2|3)?\d)-  # the day
                        ((19|20)?\d\d)  # the year (19XX - 20XX)
                        (.*?)$  # all text after the date
                        """, re.VERBOSE)

_, _, files = next(os.walk(os.getcwd()), (None, None, []))  # gets only file names and removes dir's

for file in files:
    # apply regex filter to file name
    match = datePattern.search(file)

    # skip if date doesn't exist in file name
