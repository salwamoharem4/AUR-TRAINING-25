#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time
class Mynode(Node):
    def __init__(self):
        super().__init__("counter")
        self.counter()

    def counter(self): 
        for i in range(10,-1,-1):
            if i>0:
                self.get_logger().info(f"time is {i}")
            else:
                self.get_logger().info("time is up")
            time.sleep(1.0)
def main(args=None):
    rclpy.init(args=args)
    node=Mynode()
    rclpy.spin(node)
    rclpy.shutdown()

if  __name__ == '__main__':
    main()
