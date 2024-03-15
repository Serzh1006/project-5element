
from setuptools import setup, find_packages

setup(
    name='bot',
    version='3',
    description='Very useful assisstant',
    url='https://github.com/Serzh1006/project-5element',
    author='Team_5element',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['bot=bot_setup.bot:main']}
)