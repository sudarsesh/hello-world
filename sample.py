#!/usr/bin/env python3


with open('count', 'a+') as wr:
    wr.seek(0)
    count = int(wr.read().strip())
    if count == 3:
        print('PASS: reached count = 3') 
        wr.seek(0)
        wr.truncate()
        count = 1
        wr.write(str(count))
    else:
        wr.seek(0)
        wr.truncate()
        count += 1
        wr.write(str(count))
        raise Exception('Not yet reached count of 3')
