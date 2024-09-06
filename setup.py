from setuptools import setup

package_name = 'scan_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=[
        'scan_subscriber'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='A simple subscriber node for LaserScan messages',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'scan_subscriber = scan_subscriber:main',
        ],
    },
)
