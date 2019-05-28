from setuptools import setup, find_packages

files = ["config/*"]

setup(
    name="schedulerworker",
    version="1.0.0",
    keywords=("schedulerworker"),
    description="scheduler worker",
    long_description="scheduler worker",
    license="MIT Licence",

    url="http://scheduler-worker.com",
    author="zhoubingzheng",
    author_email="zhoubingzheng@sina.com",

    packages=find_packages(),
    package_data = {'schedulerworker' : files },
    include_package_data=False,
    platforms="any",
    install_requires=[
        'requests==2.6.0',
        'apscheduler==3.6.0',
        'rq==1.0',
    ],

    scripts=[],
    entry_points={

    }
)
