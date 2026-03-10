#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class ValidationPrintingNode(Node):
    def __init__(self):
        super().__init__('Validation_printing_node')
        self.get_logger().info('Validation Printing Node has been initialized.')
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello world.')

def main(args=None):
    rclpy.init(args=args)

    node = ValidationPrintingNode()

    # node.get_logger().info('Hello world' + str(i) + '.')

    rclpy.spin(node)

    rclpy.shutdown()



if __name__ == '__main__':
    main()

