import subprocess
import os


class BLESnifferClient:
    def __init__(self, package_name=None, input_file=None):
        if input_file is not None:
            self.input_file = open(input_file, 'r')
        elif package_name is not None:
            self.adb_process = subprocess.Popen(
                ['adb', 'logcat', '-s', '-v', 'raw', 'BLESniffer_' + package_name],
                stdout=subprocess.PIPE,
            )
        else:
            raise Exception("neither package name nor file given")

    def get_evt(self):
        while True:
            if self.input_file is None:
                line = self.adb_process.stdout.readline()
                line = line.decode('utf-8')
            else:
                line = self.input_file.readline()
            parts = line.split(' ')
            if parts.__len__() < 4:
                continue
            if parts[0] != 'characteristic':
                continue
            action = parts[1]

            payload = bytearray.fromhex(''.join(parts[3:-1]))

            return {
                'action': action,
                'payload': payload,
                'characteristic': parts[2]
            }
