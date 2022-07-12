from setuptools import setup, find_packages

setup(
    name='json2xml',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='convert json to xml',
    long_description=open('README.md').read(),
    url='',
    author='zarinpy',
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
