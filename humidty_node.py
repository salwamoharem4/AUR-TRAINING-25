#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import RelativeHumidity
import random

class humidty(Node):
    def __init__(self):
        super().__init__('humidity_node')
        self.pub=self.create_publisher(RelativeHumidity,'/humidity',10)
        self.timer=self.create_timer(2.0,self.publishit)

    def publishit(self):
        humidtyval=random.uniform(20.0,100.0)
        msg=RelativeHumidity()
        msg.relative_humidity=humidtyval/100.0 #relative humidity expects value bet 0.0 , 1.0

        self.pub.publish(msg)
        self.get_logger().info(f"himidity value is {humidtyval:.1f} %")

def main (args=None):
    rclpy.init(args=args)
    node=humidty()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
        