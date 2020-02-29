rem adb tcpip 5555
rem adb connect <ip of device>:5555 shouji
rem adb connect 127.0.0.1:62001 yeshen
adb kill-server
adb connect 127.0.0.1:7555

python study.py
