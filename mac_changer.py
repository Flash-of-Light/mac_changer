#!/usr/bin/env python

import subprocess

interface = 'eth0'
new_mac = '00:11:22:33:44:88'
print('[+] changing MAC address for ' + interface + ' to the new address ' + new_mac)

subprocess.call('ifconfig ' + interface + ' down', shell=True)
subprocess.call('ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
subprocess.call('ifconfig ' + interface + ' up', shell=True)
