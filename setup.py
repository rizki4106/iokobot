from setuptools import setup

def readme():
    readme = ''
    with open("README.md") as files:
        readme = files.read()
    return readme

setup(
  name = 'iokobot',
  packages = ['iokobot'],
  version = '0.1',
  license='MIT',
  description = 'iokobot is a python library to help you make a smart bot, using machine learning algorithm',
  long_description=readme(),
  long_description_content_type="text/markdown",
  author = 'Rizki Maulana',
  author_email = 'rizkimaulana348@gmail.com',
  url = 'https://github.com/rizki4106/iokobot',
  download_url = 'https://github.com/rizki4106/iokobot/archive/v_01.tar.gz',
  keywords = ['bot', 'chatbot', 'iokobot', 'machine-learning'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ]
)