#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int32MultiArray

class MysteryClass():

    def cb1(self, topic_data: Int32MultiArray):
        self.msg1 = str(topic_data.data)

    def cb2(self, topic_data: String):
        self.msg2 = topic_data.data

    def cb3(self, topic_data: String):
        self.msg3 = topic_data.data

    def __init__(self):
        self.msg1 = ""
        self.msg2 = ""
        self.msg3 = ""
        
        self.sub1 = rospy.Subscriber('eeny', Int32MultiArray, self.cb1)
        self.sub2 = rospy.Subscriber('meeny', String, self.cb2)
        self.sub3 = rospy.Subscriber('miny', String, self.cb3)

        self.pub = rospy.Publisher('moe', String, queue_size=10)

        self.name = "mystery_node4"
        rospy.init_node(self.name)
        self.rate = rospy.Rate(1)

        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)

        self.topic_msg = String()

    def shutdownhook(self):
        self.ctrl_c = True
        print(f"{self.name} closed.")
    
    def main(self):
        while not self.ctrl_c:
            self.topic_msg = f"If only you could see what I was printing to screen... (look in the launch file)"
            rospy.loginfo("There's another node in 'src'!")
            self.pub.publish(self.topic_msg)
            self.rate.sleep()

if __name__ == "__main__":
    node = MysteryClass()
    try:
        node.main()
    except rospy.ROSInterruptException:
        pass
