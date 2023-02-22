#!/usr/bin/env python3
# Author: Gh to Ufactory parser by Romantic Technology <mo@romantic.technology>

"""
Description: 
"""

import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI


#######################################################
"""
Tests
"""
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read('../robot.conf')
        ip = parser.get('xArm', 'ip')
    except:
        ip = input('Please input the xArm ip address:')
        if not ip:
            print('input error, exit')
            sys.exit(1)
########################################################
"""
Set Up
"""

arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.reset(wait=True)

"""
Generated Movement Code:
"""
arm.set_position(x=246.498153273, y=92.3127762214, z=181.962805528, roll=3.14159265359, pitch=-0.0, yaw=1.57079632679, speed=70.0, wait=True, is_radian = True, radius=None)
arm.set_position(x=290.154687445, y=2.23837209302, z=174.970661464, roll=3.14159265359, pitch=-0.0, yaw=1.57079632679, speed=70.0, wait=True, is_radian = True, radius=None)
arm.reset(wait=True)

arm.disconnect()
