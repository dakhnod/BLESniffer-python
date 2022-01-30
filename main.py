#!/usr/bin/python3

import BLESnifferClient
import os
import sys

if __name__ == '__main__':
    # default won't find adb executable
    os.environ['PATH'] = ':'.join([os.getenv('PATH'), '/home/leinad/Android/Sdk/platform-tools/'])
    sniffer = BLESnifferClient.BLESnifferClient(sys.argv[1])
    while True:
        evt = sniffer.get_evt()
        print(evt)


