from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version= '0.1',
    author="Arnav Shukla",
    author_email="arnavshukla1011@gmail.com",
    description="SnapshotAlyzer 30000 is a tool to manage AWS EC2 snapshots",
    license="GPLc3+",
    packages=['shotty'],
    url="https://github.com/AS11-Python/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        ''',
)
