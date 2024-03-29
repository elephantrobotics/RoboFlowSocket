# encoding=utf-8
from __future__ import print_function
import sys

PYTHON_VERSION = sys.version_info[:2]
if (2, 7) != PYTHON_VERSION < (3, 5):
    print("This mycobot version requires Python2.7, 3.5 or later.")
    sys.exit(1)

import setuptools
import textwrap
import RoboFlowSocket

try:
    long_description = (
        open("README.md", encoding="utf-8").read()
        # + open("docs/README.md", encoding="utf-8").read()
    )
except:
    long_description = textwrap.dedent(
        """
        """
    )

setuptools.setup(
    name="RoboFlowSocket",
    version=RoboFlowSocket.__version__,
    author=RoboFlowSocket.__author__,
    author_email=RoboFlowSocket.__email__,
    description="用于控制mycobot pro 600，连接机械臂服务端，进行TCP/IP通讯",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=RoboFlowSocket.__git_url__,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, != 3.4.*",
)
