#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist



def left_right():
	#global velocity_publisher
	#twist = Twist()
	st1=raw_input("Enter the string")
	if st1=="left":
		print "left"
		return 10
        else:
                return 0
 
	#velocity_publisher.publish(twist)
    
    

def main():
    #global velocity_publisher
    x_lin=left_right()
    rospy.init_node('leftright') 
    twist.linear.x=x_lin
    velocity_publisher =  rospy.Publisher('/cmd_vel', Twist)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.logwarn("Running the node, time {}".format(rospy.get_time()))
        rate.sleep()
    pass

if __name__ == '__main__':
   main()
