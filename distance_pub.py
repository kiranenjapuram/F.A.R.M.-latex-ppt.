#! /usr/bin/env python
import rospy
from std_msgs.msg import Float64

def motor_start():
	pub=rospy.Publisher('motor_distance', Float64, queue_size = 10)
	motor_distance=Int32()
	rate=rospy.Rate(10)

	while not rospy.is_shutdown():
		motor_distance.data=input("enter the distance for motor=")
		pub.publish(motor_distance)
		rospy.loginfo("distance is %d cm",motor_distance.data)




if __name__=='__main__':
	try:
		rospy.init_node('motor_pose',anonymous=True)
		motor_start()
	except rospy.ROSInterruptException: pass
