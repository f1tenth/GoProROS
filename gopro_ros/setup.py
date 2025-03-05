from setuptools import find_packages, setup

package_name = 'gopro_ros'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ahmad Amine',
    maintainer_email='aminea@seas.upenn.edu',
    description='Simple ROS wrapper for publishing gopro images.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gopro_ros = gopro_ros.gopro_stream:main'
        ],
    },
)
