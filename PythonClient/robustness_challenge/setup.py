import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="airsim-robustness",
    version="1.2.8",
    author="Hadi Salman",
    author_email="hasalman@microsoft.com",
    description="Platform for AI robustness research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hadisalman/airsim",
    packages=setuptools.find_packages(),
	license='MIT',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
          'msgpack-rpc-python', 'numpy', 'opencv-contrib-python'
    ]
)
