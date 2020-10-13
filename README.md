# BLESniffer-python
BLE Sniffer android counterpart for prototyping

this library parses the output from my [xposed sniffer module](https://github.com/dakhnod/BLESniffer-android/tree/main) over adb
and creates usable events, which may be used to sketch up decoders for different BLE protocols.

#usage
for now, main.py should describe the usage quite well.
Just call it with the target package name as target:
`main.py "com.android.target.package"`