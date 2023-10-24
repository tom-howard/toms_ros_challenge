#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32MultiArray

class MysteryClass():
    def __init__(self):
        self.pub = rospy.Publisher('eeny', Int32MultiArray, queue_size=10)
        self.name = "mystery_node1"
        rospy.init_node(self.name)
        self.rate = rospy.Rate(1)

        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)

        self.topic_msg = Int32MultiArray()
        self.topic_msg.data = [13,11, 5, 6,12, 1, 7, 3, 9, 8, 2,10, 4]
        # [11, 4,13, 3, 8, 1, 9, 7, 6,12,10, 2, 5]

    def shutdownhook(self):
        self.ctrl_c = True
        print(f"{self.name} closed.")
    
    def main(self):
        timestamp = rospy.get_time()
        while not self.ctrl_c:
            self.pub.publish(self.topic_msg)
            if rospy.get_time() > timestamp + 50:
                timestamp = rospy.get_time()
            self.rate.sleep()

if __name__ == "__main__":
    node = MysteryClass()
    try:
        node.main()
    except rospy.ROSInterruptException:
        pass
