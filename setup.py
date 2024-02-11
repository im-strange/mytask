from setuptools import setup

setup(
      name="mytask",
      version="1.0.0",
      url="https://github.com/im-strange/mytask.git",
      author="Samuel Genoguin",
      description="A simple to-do app",
      py_modules=["mytask"],
      install_requires=[
          "texttable"
      ],
      include_package_data=True,
      packages=[],
      package_data={},
      entry_points={
          "console_scripts": ["mytask = mytask:main"]
      }
)
