#!/usr/bin/env python3

# lib example
from python_lib.lib_example import hello

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
from drone_controller_messages.msg import PwmMessage

def main():
    rclpy.init()
    test_node = Node("node_py_name")
    msg = PwmMessage()
    msg.front_left = 20
    msg.front_right = 2
    print(msg)

    str_publisher = test_node.create_publisher(PwmMessage, "/topicdd", 10)

    for i in range(10):
        str_publisher.publish(msg)
        time.sleep(1)

    return True


if __name__ == "__main__":
    main()


