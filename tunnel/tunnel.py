from sys                import *
from cursesmenu         import *
from cursesmenu.items   import *

import csv

class MainMenu:

    menu = CursesMenu("Turbo Tunnel v.0.1", "please select a host")
    hosts = {}
    item_count = 0

    def __init__(self): 

        with open('/home/Zach/development/python/tunnel/hosts.csv', mode = 'r') as hostfile:
            reader  = csv.reader(hostfile)
            hosts   = {rows[0]:rows[1] for rows in reader}

        for host, address in hosts.items():
            tunnel = CommandItem(host, "ssh -Y" + address)
            self.menu.append_item(tunnel)
            self.item_count += 1
        
        self.menu.show()
        return

    def printTitle(self):
        self.menu.screen.addstr(self.item_count + 5, 0, "  ______           __             ______                       __\n")
        self.menu.screen.addstr(self.item_count + 6, 0, " /_  __/_  _______/ /_  ____     /_  __/_  ______  ____  ___  / /\n")
        self.menu.screen.addstr(self.item_count + 7, 0, "  / / / / / / ___/ __ \/ __ \     / / / / / / __ \/ __ \/ _ \/ / \n")
        self.menu.screen.addstr(self.item_count + 8, 0, " / / / /_/ / /  / /_/ / /_/ /    / / / /_/ / / / / / / /  __/ /  \n")        
        self.menu.screen.addstr(self.item_count + 9, 0, "/_/  \__,_/_/  /_.___/\____/    /_/  \__,_/_/ /_/_/ /_/\___/_/   \n")
        return

#start the menu
turboTunnel = MainMenu()
