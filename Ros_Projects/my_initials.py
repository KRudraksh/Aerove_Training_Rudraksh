#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 
PI=3.14159
 
def my_initials():
    rospy.init_node('Rudraksh',anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1)
    vel=Twist()
    vel.linear.x=2.0
    vel.angular.z=1 #MKS (RADIAN/sec)
    current_angle=0
    final_angle= PI
    t0=rospy.Time.now().to_sec() #returns the current time
    while (current_angle<final_angle):
        pub.publish(vel)
        t1=rospy.Time.now().to_sec()
        current_angle=0.9*(t1-t0)
	
    vel.angular.z=PI/2
    pub.publish(vel)
    vel.linear.x=8
    vel.angilar.z=0
    pub.publish(vel)
    rospy.spin()
 
if __name__ =='__main__':
    try:
        my_initials()
    except ROSInterruptException:
        pass
    
