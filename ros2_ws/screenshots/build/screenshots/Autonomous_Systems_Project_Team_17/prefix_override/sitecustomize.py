import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/moustafaahmed13/ros2_ws/install/Autonomous_Systems_Project_Team_17'
