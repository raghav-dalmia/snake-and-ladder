from setuptools import setup

setup(
      name = "snake_and_lader",
      install_requires = ['pygame',],
      entry_points={
        'console_scripts': [
            'snl = game:start'
        ]},
         classifiers=[
                 "Programming Language :: Python :: 3"
                 ]
      )