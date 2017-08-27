#!/usr/bin/env python

import sys
import rospy
from gravity_torques.srv import *

def gravity_torques_client():
    rospy.wait_for_service('gravity_torques')
    try:
        gravity_torques = rospy.ServiceProxy('gravity_torques', GravityTorques)
        resp1 = gravity_torques()
        return resp1.gravity_torques, resp1.hysteresis_torques, resp1.crosstalk_torques, resp1.actual_torques, resp1.subtracted_torques
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    # print(gravity_torques_client('right'))
    for _ in range(1):
        print(gravity_torques_client()[4
              ])