#!/usr/bin/env python
# python thread, do not use thread moudle, use threading instead

import thread
from time import sleep

def func1():
    print 'func1'

def func2():
    print 'func2'

def main():
    print '...main...'
    thread.start_new_thread(func1, ())
    thread.start_new_thread(func2, ())
    sleep(10)
    print 'All end'

if __name__ == '__main__':
    main()
