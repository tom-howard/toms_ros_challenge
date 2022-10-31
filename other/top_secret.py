#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int32MultiArray

class topSecret():

    def cb1(self, topic_data: Int32MultiArray):
        self.seq = list(topic_data.data)
        self.got_seq = True

    def cb2(self, topic_data: String):
        self.msg = topic_data.data
        self.got_chars = True

    def __init__(self):
        self.msg = ""
        self.seq = []
                
        self.sub1 = rospy.Subscriber('some_nums', Int32MultiArray, self.cb1)
        self.sub3 = rospy.Subscriber('some_more_chars', String, self.cb2)

        self.name = "code_breaker"
        rospy.init_node(self.name)
        self.rate = rospy.Rate(0.5)

        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)

        self.topic_msg = String()

    def shutdownhook(self):
        self.ctrl_c = True
    
    def code_breaker(self, msg, sequence):
        print("Wait a sec...")
        untangled_msg = ""
        for i in sequence:
            untangled_msg = untangled_msg + msg[i-1]
        rospy.sleep(2)
        print(f"Bingo! The secret message is '{untangled_msg.upper()}'")
        self.ctrl_c = True

    def main(self):
        while not self.ctrl_c:
            self.got_seq = False
            self.got_chars = False
            print("Thinking...")
            self.rate.sleep()
            if self.got_chars and self.got_seq:
                self.code_breaker(self.msg, self.seq)
            elif self.got_chars and not self.got_seq:
                print("I need some_nums...")
            elif not self.got_chars and self.got_seq:
                print("I need some_chars...")
            else:
                print("I need some_chars and some_nums...")

if __name__ == "__main__":
    node = topSecret()
    try:
        node.main()
    except rospy.ROSInterruptException:
        pass
