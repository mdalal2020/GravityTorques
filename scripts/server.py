#!/usr/bin/env python

from gravity_torques.srv import *
import rospy
import numpy as np
from intera_core_msgs.msg import SEAJointState

def handle_gravity_torques(req):
    return GravityTorquesResponse(gravity_torques, actual_effort)

def gravity_torques_callback(data):
    global gravity_torques
    global actual_effort
    gravity_torques = np.array(data.gravity_model_effort)
    actual_effort = np.array(data.actual_effort)

def gravity_torques_server():
    rospy.init_node('gravity_torques_server')
    s = rospy.Service('gravity_torques', GravityTorques, handle_gravity_torques)
    rospy.Subscriber("robot/limb/right/gravity_compensation_torques", SEAJointState, gravity_torques_callback)
    rospy.spin()

if __name__ == "__main__":
    gravity_torques_server()