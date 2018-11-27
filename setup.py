from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cxnstr',
    version='1.1.1',
    author="Joe Boyd",
    author_email="josefuboyd@gmail.com",
    description="Parse database connection strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['cxnstr'],
    entry_points={
        'console_scripts': ['cxnstr=cxnstr:main'],
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Database",
    ],
)
