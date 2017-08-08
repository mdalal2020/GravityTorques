#!/usr/bin/env python

from gravity_torques.srv import *
import rospy
from intera_core_msgs.msg import SEAJointState
global gravity_torques

def handle_gravity_torques(req):
    return gravity_torques

def gravity_torques_callback(self, data):
    gravity_torques = np.array(data.gravity_model_effort)

# def gravity_compensation_torques(name):
#     rospy.Subscriber("robot/limb/right/gravity_compensation_torques", SEAJointState, self.gravity_torques_callback)

def gravity_torques_server():
    rospy.init_node('gravity_torques_server')
    s = rospy.Service('gravity_torques_ints', GravityTorques, handle_gravity_torques)  
    rospy.Subscriber("robot/limb/right/gravity_compensation_torques", SEAJointState, gravity_torques_callback)
    rospy.wait_for_message("robot/limb/right/gravity_compensation_torques", SEAJointState)
    rospy.spin()

if __name__ == "__main__":
    gravity_torques_server()