#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class RobotTeleop:
    def __init__(self):
        rospy.init_node('robot_teleop')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/dev/input/js1', Joy, self.joy_callback)
        self.twist = Twist()

    def joy_callback(self, joy_msg):
        linear_axis = 2  # Index for the linear axis (e.g., left stick vertical)
        angular_axis = 5  # Index for the angular axis (e.g., right stick horizontal)

        max_linear_velocity = 0.5  # Adjust this based on your robot's capabilities
        max_angular_velocity = 1.0  # Adjust this based on your robot's capabilities

        linear = joy_msg.axes[linear_axis] * max_linear_velocity
        angular = joy_msg.axes[angular_axis] * max_angular_velocity

        # Calculate linear and angular velocities for the robot
        self.twist.linear.x = linear
        self.twist.angular.z = angular

    def run(self):
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            self.pub.publish(self.twist)
            rate.sleep()

if __name__ == '__main__':
    controller = RobotTeleop()
    controller.run()

