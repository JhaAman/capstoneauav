#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class testnode:
    def __init__(self):
	#self.drivepub = rospy.Publisher('/cmd_vel', geometry_msgs/Twist.msg, queue_size=1)
	self.pubLand = rospy.Publisher('/ardrone/land',Empty,queue_size=1)
	self.pubTakeoff = rospy.Publisher('/ardrone/takeoff',Empty,queue_size=1)
	print "pubsinited"
	self.updown()
	
    def updown(self):
	self.pubTakeoff.publish(Empty)
        print "takeoff"
	rospy.sleep(10)
	self.pubLand.publish(Empty)
        print "landing"

if __name__ == '__main__':
    rospy.init_node('testnode')
    node = testnode()
   # testnode.init__(self)
   # rospy.spin()
