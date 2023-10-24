#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int32MultiArray

class topSecret():

    def numbers_callback(self, topic_data: Int32MultiArray):
        self.seq = list(topic_data.data)
        self.got_numbers = True

    def letters_callback(self, topic_data: String):
        self.msg = topic_data.data
        self.got_letters = True

    def __init__(self):
        self.msg = ""
        self.seq = []
                
        self.some_numbers = rospy.Subscriber('topic_a', Int32MultiArray, self.numbers_callback)
        self.some_letters = rospy.Subscriber('topic_b', String, self.letters_callback)

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
            self.got_numbers = False
            self.got_letters = False
            print("OK...")
            self.rate.sleep()
            if self.got_letters and self.got_numbers:
                self.code_breaker(self.msg, self.seq)
            elif self.got_letters and not self.got_numbers:
                print("I need some numbers...")
            elif not self.got_letters and self.got_numbers:
                print("I need some letters...")
            else:
                print("I need some letters and some numbers...")

if __name__ == "__main__":
    node = topSecret()
    try:
        node.main()
    except rospy.ROSInterruptException:
        pass
