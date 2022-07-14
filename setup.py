from setuptools import find_packages, setup


setup(
    name='json2xml',
    version='0.1',
    packages=find_packages(exclude="tests*"),
    include_package_data=True,
    license='MIT',
    description='convert json to xml',
    url='https://github.com/zarinpy/json2xml',
    author='zarinpy',
    extras_require={
        'test': ['pytest'],
    },
    author_email='zarinpy@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    py_modules=['json2xml.src:Json2Xml'],
)
