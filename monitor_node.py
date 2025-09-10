#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import FluidPressure,RelativeHumidity
from std_msgs.msg import Int32

class monitor(Node):
    def __init__(self):
        super().__init__('monitor_node')
        self.temp_sub=self.create_subscription(Int32,'/temperature',self.temp_callback,10)
        self.humd_sub=self.create_subscription(RelativeHumidity,'/humidity',self.humd_callback,10)
        self.press=self.create_subscription(FluidPressure,'/pressure',self.press_callback,10)

        self.temprature=None
        self.humidty=None
        self.pressure=None
    def temp_callback(self,msg):
        self.temprature=msg.data
        self.combined_read()


    def humd_callback(self,msg):
        self.humidty=msg.relative_humidity *100.0
        self.combined_read()
    
    def press_callback(self,msg):
        self.pressure=msg.fluid_pressure /100.0
        self.combined_read()

    def combined_read(self):
        message=(f"temp= {self.temprature} °C, humidity ={self.humidty} %, pressure = {self.pressure} hpa")
        self.get_logger().info(message)

        with open("reading.txt","a")as file:
            file.write(message+ "\n")
def main (args=None):
    rclpy.init(args=args)
    node=monitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()