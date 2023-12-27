from setuptools import setup, find_packages

setup(
    name='g_log',
    version='1.0',
    author='Jakob Balkovec',
    description='Logging library for Python',
    long_description='''The g_log library provides functionality for logging messages with different severity levels.''',
    url='https://github.com/j-balkovec/Projects/tree/main/Logger',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
