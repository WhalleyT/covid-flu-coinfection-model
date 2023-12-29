from setuptools import setup, find_packages

print("Hello")
print(find_packages())

setup(
    name="covid-influenza-coinfection-model",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open('requirements.txt')
        ]
)
