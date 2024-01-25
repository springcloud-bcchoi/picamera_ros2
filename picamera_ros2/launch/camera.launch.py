
import os
import sys
import launch
import launch_ros.actions
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    launch_args = [
        DeclareLaunchArgument(
            "video_width",
            default_value="1280",
            description="Width of the video stream."
        ),
        DeclareLaunchArgument(
            "video_height",
            default_value="720",
            description="Height of the video stream."
        ),
        DeclareLaunchArgument(
            "framerate",
            default_value="30",
            description="Framerate of the video stream."
        ),
        DeclareLaunchArgument(
            "frame_id",
            default_value="camera_frame",
            description="Frame ID of the camera."
        ),
        DeclareLaunchArgument(
            "topic_name",
            default_value="image_raw",
            description="Topic name for the camera images."
        ),
    ]

    container = ComposableNodeContainer(
        name='picamera_ros2_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='picamera_ros2',
                plugin='picamera_ros::PiCameraROS',
                name='picamera_ros2',
                parameters=[{
                    'video_width': LaunchConfiguration('video_width'),
                    'video_height': LaunchConfiguration('video_height'),
                    'framerate': LaunchConfiguration('framerate'),
                    'frame_id': LaunchConfiguration('frame_id'),
                    'topic_name': LaunchConfiguration('topic_name'),
                }]
            ),
        ],
        output='screen',
    )
    return launch.LaunchDescription(
        launch_args +
        [
            container
        ]
    )
