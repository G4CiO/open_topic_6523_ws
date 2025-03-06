#!/usr/bin/python3

from carla_mapping.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, Imu, NavSatFix
from nav_msgs.msg import Odometry


class IncreasePubRate(Node):
    def __init__(self):
        super().__init__('increase_pub_rate')

        # Subscribers
        self.pointcloud_sub = self.create_subscription(PointCloud2, '/sensing/lidar/top/pointcloud_raw', self.pointcloud_callback, 10)
        self.imu_sub = self.create_subscription(Imu, '/sensing/imu/tamagawa/imu_raw', self.imu_callback, 10)
        self.odom_sub = self.create_subscription(Odometry, '/carla/ego_vehicle/odometry', self.odom_callback, 10)
        self.gps_sub = self.create_subscription(NavSatFix, '/sensing/gnss/ublox/nav_sat_fix', self.gps_callback, 10)

        # Publishers
        self.pointcloud_pub = self.create_publisher(PointCloud2, '/pointcloud_out', 10)
        self.imu_pub = self.create_publisher(Imu, '/imu_out', 10)
        self.odom_pub = self.create_publisher(Odometry, '/odom_out', 10)
        self.gps_pub = self.create_publisher(NavSatFix, '/gps_out', 10)

        # Latest messages storage
        self.latest_pointcloud = None
        self.latest_imu = None
        self.latest_odom = None
        self.latest_gps = None

        # Timer at 200 Hz
        self.timer = self.create_timer(0.005, self.timer_callback)  # 200 Hz

    def pointcloud_callback(self, msg):
        self.latest_pointcloud = msg

    def imu_callback(self, msg):
        self.latest_imu = msg

    def odom_callback(self, msg):
        self.latest_odom = msg

    def gps_callback(self, msg):
        self.latest_gps = msg

    def timer_callback(self):
        # Publish each topic if available
        if self.latest_pointcloud is not None:
            self.pointcloud_pub.publish(self.latest_pointcloud)
        if self.latest_imu is not None:
            self.imu_pub.publish(self.latest_imu)
        if self.latest_odom is not None:
            self.odom_pub.publish(self.latest_odom)
        if self.latest_gps is not None:
            self.gps_pub.publish(self.latest_gps)

def main(args=None):
    rclpy.init(args=args)
    node = IncreasePubRate()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
