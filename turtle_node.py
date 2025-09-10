#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist #twist represnt velocity (x,y,z)
import sys, termios ,tty

class move_turtle2(Node):

    def __init__(self):
        super().__init__("move_turtle")
        self.moveit=self.create_publisher(Twist,"/turtle2/cmd_vel",10)
        self.settings = termios.tcgetattr(sys.stdin)

    def get_key(self):
        tty.setraw(sys.stdin.fileno()) #change mode from cooked to raw
        key=sys.stdin.read(1) #reads one char frim stdin
        termios.tcsetattr(sys.stdin ,termios.TCSADRAIN,self.settings) #restore terminal settings
        return key

    def run_turtle(self):
        print("Control the turtle with WASD keys. Press 'q' to quit.")
        try:
            while True:
                key = self.get_key()
                twist = Twist()
                if key == 'w':
                    twist.linear.x = 2.0
                elif key == 's':
                    twist.linear.x = -2.0
                elif key == 'd':
                    twist.angular.z = -2.0  
                elif key == 'a':
                    twist.angular.z = 2.0   
                elif key == 'q':
                    break
                self.moveit.publish(twist)
        finally:
            # Stop the turtle when quitting (runned after we hot q or ctrl c or any error)
            self.moveit.publish(Twist())
            print("\nShutting down. Turtle stopped.")
#without finally I will still in raw mode 


def main (args=None):
    rclpy.init(args=args)
    node=move_turtle2()
    node.run_turtle()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    