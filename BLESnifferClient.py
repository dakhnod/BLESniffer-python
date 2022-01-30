import subprocess
import json


class BLESnifferClient:
    def __init__(self, package_name=None, input_file=None):
        self.input_file = None
        if input_file is not None:
            self.input_file = open(input_file, 'r', encoding='utf-8')
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

            if not line.startswith('event '):
                continue

            line = line[6:]

            try:
                event_object = json.loads(line)

                return {
                    'action': event_object['event'],
                    'data': event_object['data'],
                }
            except json.JSONDecodeError:
                print("error deconding line %s" % line)
