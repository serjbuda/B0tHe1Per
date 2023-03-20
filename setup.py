from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'bot_helper=my_package.bot_interface:run'
        ]
    }
)
