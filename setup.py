from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='nutellaML',
    version='0.1',
    description='nutella service sdk',
    author='kitoha',
    author_email='kth004@naver.com',
    url='https://github.com/NutellaCoder/NutellaSdk',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['nutellaML'],
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)