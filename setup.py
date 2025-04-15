from setuptools import setup, find_packages

setup(
  name='CommonLib',
  version='1.0.0',
  packages=find_packages(),
  install_requires=[],  # add dependencies like ['requests']
  author='Rugbeat90999',
  author_email='rugbeat909@gmail.com',
  description='A library of different functions and classes for my projects',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/Rugbeat90999/CommonLib',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.12',
)
