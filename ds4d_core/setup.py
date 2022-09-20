from setuptools import setup

package_name = 'ds4d_core'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Test',
    maintainer_email='test@test.org',
    description='ROS 2 humble driver for the DualShock 4 controller',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo            = ds4d_core.demo:main',
            'ds4_driver_node = ds4d_core.ds4_driver_node:main',
            'ds4_twist_node  = ds4d_core.ds4_twist_node:main'
        ],
    },
)
