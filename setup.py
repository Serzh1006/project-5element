
from setuptools import setup, find_packages

setup(
    name='bot',
    version='3',
    description='Very useful assisstant',
    url='http://github.com/dummy_user/useful',
    author='Team_5element',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['bot=bot:main']}
)

