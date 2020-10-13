#!/usr/bin/env python3

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Development"

#V={(V}_C,V_M,V_D,V_T)
#L=M_N * (V_1+ V_2 + ... + V_N)

import configparser

class virtual_machine():
    def __init__(self, cpu, ram, disk, nic):
        self._cpu = cpu
        self._ram = ram #assume given in MB
        self._disk = disk #assume given in GB
        self._nic = nic

def get_scalars():
    #read config
    cpu = 
    ram = 
    scalars = (cpu, ram)
    return scalars

def get_scenario():
    #prompt user
    #iteratively build collection of vm in scenario


def estimate_compute():
    # number of vms

if __name__ == "__main__":
