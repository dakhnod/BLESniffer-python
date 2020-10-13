import subprocess
import os


class BLESnifferClient:
    def __init__(self, package_name):
        self.adb_process = subprocess.Popen(
            ['adb', 'logcat', '-s', '-v', 'raw', 'BLESniffer_' + package_name],
            stdout=subprocess.PIPE,
        )

    def get_evt(self):
        while True:
            line = self.adb_process.stdout.readline()
            line = line.decode('utf-8')
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

