from setuptools import find_packages, setup

setup(
    name="x2vlm-gml",
    version="0.1.0",
    author="Gimlet Labs",
    url="https://github.com/gimletlabs/X2-VLM",
    license="BSD",
    description="Package for X2-VLM, a vision-language model from ByteDance",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
