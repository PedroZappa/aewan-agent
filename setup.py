from setuptools import setup, find_packages

setup(
  name="aewan-agent",
  version="0.1.0",
  description="Aewan Agent",
  author="Zedr0",
  # package_dir={"": "app"},
  # packages=find_packages(include=["app.*"]),
  # include_package_data=True,
  scripts=[
    "scripts/build.sh",
    "scripts/run.sh",
  ],
  install_requires=[
    "setuptools",
    "colorama",
  ],
  extras_require={
    "dev": ["debugpy", "ruff"],
  },
)

