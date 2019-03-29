#!/usr/bin/env python

import subprocess

interface = input("interface > ")
new_mac = input("new MAC > ")
print('[+] changing MAC address for ' + interface + ' to the new address ' + new_mac)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])

# fixes the vulnerability by allowing no additional commands

# subprocess.call('ifconfig ' + interface + ' down', shell=True)
# subprocess.call('ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
# subprocess.call('ifconfig ' + interface + ' up', shell=True)

# this format of subprocess is vulnerable to command injections
# interface = eth0;ls; will add in an ls command
