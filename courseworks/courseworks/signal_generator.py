import rclpy
import numpy as np
from rclpy.node import Node 
from std_msgs.msg import String 
from std_msgs.msg import Float32

class My_Publisher(Node):
    def __init__(self):
        super().__init__("signal_generator_node")
        self.publisher_signal = self.create_publisher(Float32, "signal", 10) 
        self.publisher_time = self.create_publisher(Float32, "time", 10)   
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.timer2 = self.create_timer(timer_period, self.timer_callback2)
        self.get_logger().info("Signal generator node succesfully initialized!!!")
        self.msg_signal = Float32()
        self.msg_time = Float32()
        self.time = 0.0
    
    def timer_callback(self):
        self.time += 0.1 
        self.msg_time.data = self.time
        self.publisher_time.publish(self.msg_time)
        signal = np.sin(self.time)
        self.msg_signal.data = signal
        self.publisher_signal.publish(self.msg_signal)

    #def timer_callback2(self):
    #    signal = np.sin(self.time)
    #    self.msg_signal.data = signal
    #    self.publisher_signal.publish(self.msg_signal)
       

def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
