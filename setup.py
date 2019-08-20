import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="influxdb_pytest_plugin",
    version="0.0.16",
    author="Strike Team",
    author_email="elenaramyan@workfront.com",
    description="Plugin for influxdb and pytest integration",
    url="https://gitlab.workfront.tech/globalqa/influxdb-grafana-reporting/influxdb-pytest",
    packages=['influxdb_pytest_plugin'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=['pytest', 'pytest-xdist'],
    entry_points={'pytest11': ['influxdb-pytest = influxdb_pytest_plugin.influxdb_pytest_plugin', ], },
)