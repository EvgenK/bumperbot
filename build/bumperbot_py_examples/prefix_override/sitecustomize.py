import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/emkorogodsky/ros2_ws/src/install/bumperbot_py_examples'
