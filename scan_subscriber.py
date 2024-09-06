import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanSubscriber(Node):
    def __init__(self):
        super().__init__('scan_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',  # Topic name to subscribe to
            self.listener_callback,
            10)  # QoS
        self.subscription  # To prevent it from being garbage collected

    def listener_callback(self, msg):
        # Log the number of range readings
        self.get_logger().info(f'Received scan data: {len(msg.ranges)} ranges')

def main(args=None):
    rclpy.init(args=args)
    node = ScanSubscriber()
    rclpy.spin(node)  # Keep the node alive to receive data
    node.destroy_node()
    rclpy.shutdown()  # Clean up and shut down

if __name__ == '__main__':
    main()
