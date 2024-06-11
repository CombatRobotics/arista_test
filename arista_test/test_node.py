import rclpy
from rclpy.node import Node

from std_msgs.msg import Header
from sensor_msgs.msg import JointState
import time

class TestJointPublisher(Node):

    def __init__(self):

        self.joint_states=JointState()
        self.joint_states.name=[" "]*6
        self.joint_states.velocity=[0.0]*6
        self.name_l=["right_front", "right_mid", "right_back", "left_front", "left_mid", "left_back"]
        self.velocity_l=[10,10,12,12,12,10]
        super().__init__('test_publisher')
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.skip_list=[4,5]
        self.i = 0
        

    def timer_callback(self):
        # self.joint_states.velocity.clear()
        # self.joint_states.name.clear()
        # self.joint_states.velocity.clear()
        # self.joint_states.name=[" "]*6
        # self.joint_states.velocity=[0.0]*6
        # current_time = time.time() - self.start_time
        # self.joint_states.header.stamp = self.get_clock().now().to_msg()
        for i in range(6):
            if(i in self.skip_list):

                continue
            else:
                 self.joint_states.name[i]=self.name_l[i]
                 self.joint_states.velocity[i]=self.velocity_l[i]
                 self.get_logger().info('Publishing')
        
        # msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(self.joint_states)
        
        
        # self.i += 1


def main(args=None):
    rclpy.init(args=args)

    test_publisher = TestJointPublisher()

    rclpy.spin(test_publisher)
    test_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()