#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import FluidPressure
import random

class pressure(Node):
    def __init__(self):
        super().__init__('pressure_node')
        self.pub=self.create_publisher(FluidPressure,'/pressure',10)
        self.timer=self.create_timer(3.0,self.publishit)

    def publishit(self):
        pressureval=random.uniform(900.0,1100.0)
        msg=FluidPressure()
        msg.fluid_pressure = pressureval * 100.0 #convert it to pa

        self.pub.publish(msg)
        self.get_logger().info(f"pressure level is {pressureval:.1f} hpa")

def main (args=None):
    rclpy.init(args=args)
    node=pressure()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
        
