from setuptools import setup
import codecs

with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='aio-doh',
    url='https://github.com/ZhukovAlexander/aio-doh',
    author='Alexander Zhuko',
    author_email='zhukovaa90@gmail.com',
    description='Asynchronous DNS-over-HTTPS client for Python',
    long_description=readme,
    keywords='python dns https asyncio',
    use_scm_version=True,
    python_requires=">=3.6",
    setup_requires=['setuptools_scm'],
    install_requires=['aiohttp'],
    packages=['doh',],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
