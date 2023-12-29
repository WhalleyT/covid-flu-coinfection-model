from setuptools import setup, find_packages

print("Hello")
print(find_packages())

setup(
    name="covid-influenza-coinfection-model",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "bokeh==3.2.2",
        "numpy",
        "scipy"
        ]
)
