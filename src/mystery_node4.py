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
        
        self.sub1 = rospy.Subscriber('some_nums', Int32MultiArray, self.cb1)
        self.sub2 = rospy.Subscriber('some_chars', String, self.cb2)
        self.sub3 = rospy.Subscriber('some_more_chars', String, self.cb3)

        self.pub = rospy.Publisher('conclusions', String, queue_size=10)

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
            self.topic_msg = f"My conclusion is: I can see three topics, but I've no idea what to do with them! (Need a hint: look in src...))"
            self.pub.publish(self.topic_msg)
            self.rate.sleep()

if __name__ == "__main__":
    node = MysteryClass()
    try:
        node.main()
    except rospy.ROSInterruptException:
        pass
