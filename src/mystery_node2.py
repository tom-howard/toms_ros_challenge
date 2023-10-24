#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class MysteryClass():
    def __init__(self):
        self.pub = rospy.Publisher('meeny', String, queue_size=10)
        self.name = "mystery_node2"
        rospy.init_node(self.name)
        self.rate = rospy.Rate(1)

        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)

        self.topic_msg = String()
        self.topic_msg.data = "tncytk uhkiak"

    def shutdownhook(self):
        self.ctrl_c = True
        print(f"{self.name} closed.")
    
    def main(self):
        timestamp = rospy.get_time()
        while not self.ctrl_c:
            self.pub.publish(self.topic_msg)
            if rospy.get_time() > timestamp + 120:
                timestamp = rospy.get_time()
            self.rate.sleep()

if __name__ == "__main__":
    node = MysteryClass()
    try:
        node.main()
    except rospy.ROSInterruptException:
        pass
