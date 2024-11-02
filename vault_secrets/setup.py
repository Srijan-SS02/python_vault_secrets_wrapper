from setuptools import setup, find_packages

setup(
    name="vault_secrets",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "vault-secrets=vault_secrets.cli:main",
        ],
    },
    author="Srijan Srivastava",
    author_email="codeofficialsrijansriv@gmail.com",
    description="A simple CLI tool to retrieve secrets from HashiCorp Vault",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vault-secrets",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
