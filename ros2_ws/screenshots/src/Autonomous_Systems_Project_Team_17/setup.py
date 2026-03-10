from setuptools import find_packages, setup

package_name = 'Autonomous_Systems_Project_Team_17'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='moustafaahmed13',
    maintainer_email='moustafaabuelmagd1@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'Validation_printing_node = Autonomous_Systems_Project_Team_17.Validation_Printing_Node_Team_17:main',
        ],
    },
)
