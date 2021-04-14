from setuptools import setup


def readme():
    readme = ''
    with open("README.md") as files:
        readme = files.read()
    return readme


setup(
    name='ioko',
    packages=['ioko'],
    version='0.7',
    license='MIT',
    description='ioko is a python library to help you make a smart bot, using machine learning algorithm',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Rizki Maulana',
    author_email='rizkimaulana348@gmail.com',
    url='https://github.com/rizki4106/ioko',
    download_url='https://github.com/rizki4106/ioko/archive/v_01.tar.gz',
    keywords=['bot', 'chatbot', 'ioko', 'machine-learning'],
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
