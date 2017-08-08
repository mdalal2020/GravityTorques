#!/usr/bin/env python

from gravity_torques.srv import *
import rospy
import numpy as np
from intera_core_msgs.msg import SEAJointState

def handle_gravity_torques(req):
    torques = gravity_compensation_torques(req.name)
    return GravityTorquesResponse(torques)

def gravity_torques_callback(data):
    gravity_torques = np.array(data.gravity_model_effort)
    return gravity_torques

def gravity_compensation_torques(name):
    torques=  rospy.wait_for_message("robot/limb/right/gravity_compensation_torques", SEAJointState)
    return torques.gravity_model_effort

def gravity_torques_server():
    rospy.init_node('gravity_torques_server')
    s = rospy.Service('gravity_torques', GravityTorques, handle_gravity_torques)
    rospy.spin()

if __name__ == "__main__":
    gravity_torques_server()