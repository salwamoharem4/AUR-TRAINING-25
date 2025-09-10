#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random
class temp(Node):
    def __init__(self):
        super().__init__("temperature")
        self.pub=self.create_publisher(Int32,'/temperature',10)
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        msg=Int32()
        msg.data=random.randint(15,40)
        self.pub.publish(msg)
        self.get_logger().info(f"temp is {msg.data} °C")
def main (args=None):
    rclpy.init(args=args)
    node=temp()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
        
