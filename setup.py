from setuptools import setup
from os import path

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="efitness_sniper",
    version="0.2",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["efitness_sniper"],
    license="MIT",
    author="Marek Wajdzik",
    author_email="marek@wajdzik.eu",
    description="eFitness.com.pl Booking sniper",
    entry_points={"console_scripts": ["efitness=efitness_sniper.app:main"],},
    keywords = ['efitness', 'sniper', 'booking', 'bookings'],
    download_url= "https://github.com/consi/efitness-sniper/archive/0.2.tar.gz",
    classifiers=[
        'Development Status :: 4 - Beta', 
        'Intended Audience :: End Users/Desktop', 
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.7',
  ],
)
