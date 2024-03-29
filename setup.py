
from setuptools import setup, find_packages

setup(
      name="mytask",
      version="1.0.0",
      url="https://github.com/im-strange/mytask.git",
      author="im-strange",
      description="A simple to-do app",
      py_modules=["mytask"],
      install_requires=[
          "texttable"
      ],
      packages=find_packages(),
      package_data={"mytask":["data/*"]},
      include_package_data=True,
      entry_points={
          "console_scripts": ["mytask = mytask.mytask:main"]
      }
)
