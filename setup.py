from setuptools import setup, find_namespace_packages

with open('README.md', 'r') as file:
    long_description = file.read()

# with open('requirements.txt') as f:
#     required = f.read().splitlines()

setup(name='stathem_bot',
      version='0.0.2', # major.minor.patch
      description="Stathem GPT generator",
      long_description=long_description,
      url='https://github.com/nickolas-z/wolf357',
      author='nickolas-z, vlad-bb',
      author_email='vlad_bb@icloud.com',
      license='MIT',
      packages=find_namespace_packages(),
      classifiers=["Programming Language :: Python :: 3"],
      install_requires=['colorama==0.4.6', 'openai==1.35.13'], # required todo find why FileNotFoundError: [Errno 2] No such file or directory: 'requirements.txt'
      include_package_data=True,
      package_data={"": ["*.txt"]},
      entry_points={"console_scripts": ["sttm = stathem_bot:main"]},
    )