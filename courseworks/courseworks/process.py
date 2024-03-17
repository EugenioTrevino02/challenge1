import rclpy
import numpy as np
from rclpy.node import Node 
from std_msgs.msg import Float32 

class My_Process(Node): 
    def __init__(self):
        super().__init__("process_node")
        self.sub_signal = self.create_subscription(Float32, "signal", self.signal_callback, 10)
        self.sub_time = self.create_subscription(Float32, "time", self.time_callback, 10)
        self.publisher_proc_signal = self.create_publisher(Float32, "proc_signal", 10) 
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info("Process node initialized!!!")
        self.msg_proc_signal = Float32()
        self.current_time = 0.0

    def signal_callback(self, msg_signal): 
        self.get_logger().info("Signal: {}".format(msg_signal.data))

    def time_callback(self, msg_time): 
        self.get_logger().info("Time: {}".format(msg_time.data))
        self.current_time = msg_time.data
        
    def timer_callback(self): 
        proc_signal = np.sin(self.current_time) * np.cos(np.pi) + np.cos(self.current_time) * np.sin(np.pi)
        self.msg_proc_signal.data = proc_signal
        self.publisher_proc_signal.publish(self.msg_proc_signal) 



def main(args=None):
    rclpy.init(args=args)
    m_s = My_Process()
    rclpy.spin(m_s)
    m_s.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 
