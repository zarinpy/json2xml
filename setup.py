from setuptools import setup, find_packages

setup(
    name='json2xml',
    version='0.1',
    packages=find_packages(exclude="tests*"),
    include_package_data=True,
    license='MIT',
    description='convert json to xml',
    url='https://github.com/zarinpy/json2xml',
    author='zarinpy',
    author_email='zarinpy@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.10',
    ],
    py_modules=['json2xml.src:Json2Xml'],
)
