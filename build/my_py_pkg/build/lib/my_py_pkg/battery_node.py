#!/usr/bin/env python3
from functools import partial
import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import LedSwitch

class BatteryNode(Node):

    def __init__(self):
        super().__init__("battery_node")
        self.isCharged = True
        self.get_logger().info("Battery node started")
        self.create_timer(6, self.timer_callback)

    def timer_callback(self):
        self.isCharged = not self.isCharged
        self.call_led_node(led_number=3, state=self.isCharged)
    
    def call_led_node(self, led_number, state):
        client = self.create_client(LedSwitch, "led_switch")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for server led switch")
        
        request = LedSwitch.Request()
        request.led_number = led_number
        request.switched_on = state

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_led_switch, led_number=led_number, state=state))

    def callback_led_switch(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info("Led number: " + str(led_number) + " Request: " + str(state) + " Success: " + str(response.success))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()