import rclpy
from rclpy.executors import ExternalShutdownException

def main(args=None):
	try:
		with rclpy.init(args=args):
			node = rclpy.create_node("swarm_manager_node")
			
	except (KeyboardInterrupt, ExternalShutdownException
		pass
		
if __name__ == "__main__":
	main()
