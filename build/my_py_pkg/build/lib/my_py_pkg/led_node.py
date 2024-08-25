#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import LedSwitch
from my_robot_interfaces.msg import LedState

class LedNode(Node):

    def __init__(self):
        super().__init__("led_node")
        self.server_ = self.create_service(LedSwitch, "led_switch", self.callback_led_switch)
        self.get_logger().info("Led node initiated")
        self.publisher_ = self.create_publisher(LedState, "led_state", 10)
        self.create_timer(3, self.timer_callback)
        self.led_array=[False, False, False]
    
    def callback_led_switch(self, request, response):
        led_index = request.led_number - 1
        self.led_array[led_index] = request.switched_on
        response.success = True
        self.get_logger().info("Led number: " + str(request.led_number) + " Request: " + str(request.switched_on) + " Success: " + str(response.success))
        return response
    
    def timer_callback(self):
        msg = LedState()
        msg.led_one_is_active = self.led_array[0]
        msg.led_two_is_active = self.led_array[1]
        msg.led_three_is_active = self.led_array[2]
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LedNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()