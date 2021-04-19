'''
To run the job:

$ pyats run job IOS_XE_magic_carpet_job.py --testbed-file testbed/testbed_ios_xe.yaml

'''

import os
from genie.testbed import load
from ascii_art import GREETING, RUNNING, FINISHED
from pyats import topology
from genie.conf import Genie


def main(runtime):

    # ----------------
    # Load the testbed
    # ----------------
    if not runtime.testbed:
        # If no testbed is provided, load the default one.
        # Load default location of Testbed
        testbedfile = os.path.join('testbed/testbed.yaml')
        testbed = load(testbedfile)

    else:
        # Use the one provided
        testbed = runtime.testbed


    #Device list store 
    IOS_XE = []
    F5 = []
    JUNOS = []
    
    #sort devices based on OS
    for device in testbed:
        if testbed.devices[f'{device.name}'].os == 'iosxe':
            IOS_XE.append(device.name)
            
        elif testbed.devices[f'{device.name}'].os == 'BIGIP':
            F5.append(device.name)

        elif testbed.devices[f'{device.name}'].os == 'junos':
            JUNOS.append(device.name)
        


    #Testscripts
    testscript_iosxe = os.path.join(os.path.dirname(__file__), 'magic_carpet_scripts/IOS_XE_magic_carpet.py')
    testscript_f5 = os.path.join(os.path.dirname(__file__), 'magic_carpet_scripts/F5_magic_carpet.py')
    testscript_junos = os.path.join(os.path.dirname(__file__), 'magic_carpet_scripts/JUNOS_magic_carpet.py')
    
    # run script
    if len(IOS_XE) !=0:
        runtime.tasks.run(testscript=testscript_iosxe, testbed=testbed)
    if len(F5) != 0:
        runtime.tasks.run(testscript=testscript_f5, testbed=testbed)
    if len(JUNOS) != 0:
        runtime.tasks.run(testscript=testscript_junos, testbed=testbed)

    