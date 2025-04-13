from setuptools import setup, find_packages

setup(
    name="anythingpassword",
    version="0.2.1",
    packages=find_packages(),
    install_requires=[
        "cryptography==44.0.2",
    ],
    entry_points={
        "console_scripts": [
            "anythingpassword=anythingpassword.cli:cli",
        ],
    },
    author="Akinboye Yusuff",
    author_email="mailakinboye@gmail.com",
    description="This Python application provides a suite of tools for generating, analyzing, encrypting, and managing passwords securely. It includes functionality to generate strong random passwords, evaluate password strength, calculate password entropy and crack time, check for password expiration, and detect common passwords. Additionally, it supports secure password encryption and decryption using the Fernet symmetric encryption algorithm, with the encryption key stored securely in the same directory as the script. The application is designed to be modular, secure, and user-friendly, with robust error handling and platform compatibility (Unix-like systems and Windows).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/akinboye/anythingpassword",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)