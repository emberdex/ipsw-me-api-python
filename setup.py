from setuptools import setup, find_packages

setup(
    name='ipsw_me_client',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='emberdex',
    author_email='tobes+ipswclient@emberdex.st',
    description='A fully-featured, asynchronous client library for the ipsw.me API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.10'
)
