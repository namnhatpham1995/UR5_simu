#!/usr/bin/env python
import numpy as np
import rospy
from std_msgs.msg import String
from control_msgs.msg import JointTrajectoryControllerState
def ur5pub():
    pub = rospy.Publisher('/arm_controller/state', JointTrajectoryControllerState, queue_size=10)
    rospy.init_node('ur5pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	msg = JointTrajectoryControllerState() # make represented message variable from library
	msg.joint_names=[elbow_joint, shoulder_lift_joint, shoulder_pan_joint, wrist_1_joint, 
			wrist_2_joint, wrist_3_joint] #add name of joints
	desired_joints = [1,1,1,1,1,1] #add desired coordinates to publish for 6 joints
        msg.desired.positions = np.sin(desired_joints); #add sine waves of all joints to variable
        rospy.loginfo(msg) # print message which will be published
        pub.publish(msg) # publish message
        rate.sleep()

if __name__ == '__main__':
    try:
        ur5pub()
    except rospy.ROSInterruptException:
        pass
