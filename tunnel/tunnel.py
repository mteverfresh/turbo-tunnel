from sys                import *
from cursesmenu         import *
from cursesmenu.items   import *

import time
import csv
import argparse
import subprocess

PATH = '/home/Zach/development/python/hosts.csv'

class MainMenu:

    menu = CursesMenu("Turbo Tunnel v.0.1", "please select a host")
    hosts = {}
    item_count = 0

    def __init__(self, args): 

        with open(PATH, mode = 'r') as hostfile:
            reader  = csv.reader(hostfile)
            hosts   = {rows[0]:rows[1] for rows in reader}

        for host, address in hosts.items():
            if '-a' in args:
                tunnel = CommandItem(host, "ssh -" + args + " " + address)
            else:
                tunnel = CommandItem(host, "ssh " + address)

            self.menu.append_item(tunnel)
            self.item_count += 1
        
        self.menu.show()
        return

def printVersion():
    print("  ______           __             ______                       __")
    print(" /_  __/_  _______/ /_  ____     /_  __/_  ______  ____  ___  / /")
    print("  / / / / / / ___/ __ \/ __ \     / / / / / / __ \/ __ \/ _ \/ / ")
    print(" / / / /_/ / /  / /_/ / /_/ /    / / / /_/ / / / / / / /  __/ /  ")        
    print("/_/  \__,_/_/  /_.___/\____/    /_/  \__,_/_/ /_/_/ /_/\___/_/   ")
    print("\nVersion 0.1\n")
    return

#start the menu
argparser = argparse.ArgumentParser(description = "Easily ssh to remote hosts")
argparser.add_argument("-a", "--args", help="the ssh args to use when tunneling")
argparser.add_argument("-v", "--version", action='store_true', help="show the version")
argparser.add_argument("-n", "--new", nargs=2, help="add a new name/hostname+address pair to the hosts.csv file")

rawargs = argparser.parse_args()
args = vars(rawargs)

if '-v' in args:
    printVersion()
    sys.exit()
elif '-n' in args:
    with open(PATH, mode = 'a') as hostfile:
        writer = csv.writer(hostfile)
        writer.writerow(args['-n'][0] + ", " + args['-n'][1])
    sys.exit()
else:
    printVersion()
    time.sleep(1)
    turboTunnel = MainMenu(args)
