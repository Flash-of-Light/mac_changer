#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface', help='Interface to change MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')

    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error('You need to specificy an interface (--help for more info)')
    elif not options.new_mac:
        parser.error('You need to specificy a new MAC address (--help for more info)')
    return options

def change_mac(interface, new_mac):
    print('[+] changing MAC address for ' + interface + ' to the new address ' + new_mac)

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

options = get_arguments()
change_mac(options.interface, options.new_mac)

# interface = options.interface
# new_mac = options.new_mac

# subprocess.call('ifconfig ' + interface + ' down', shell=True)
# subprocess.call('ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
# subprocess.call('ifconfig ' + interface + ' up', shell=True)

