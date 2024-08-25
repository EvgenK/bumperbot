from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robots = ["C3PO", "R2D2", "Atlas", "Spot", "Megatron"]

    for robot in robots:
        ld.add_action(Node(
            package="my_py_pkg",
            executable="robot_news_station",
            name="robot_news_station_" + str(robot),
            parameters=[
                {"robot_name": robot}
            ]
        ))

    smartphone_node = Node(
        package="my_py_pkg",
        executable="smartphone",
        name="smartphone"
    )

    ld.add_action(smartphone_node)
    return ld