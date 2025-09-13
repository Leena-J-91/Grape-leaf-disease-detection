from setuptools import setup, find_packages

setup(
    name="grape-disease-detection",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.28.1",
        "tensorflow-cpu==2.15.0",
        "numpy==1.24.3",
        "Pillow==10.0.0",
    ],
    python_requires=">=3.8,<3.12",
)
