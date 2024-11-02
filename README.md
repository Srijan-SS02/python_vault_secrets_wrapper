# Vault Secrets CLI

`Vault Secrets CLI` is a Python package that provides a simple, interactive command-line interface (CLI) to retrieve secrets from HashiCorp Vault. It supports access to Vault's Key/Value (KV) v2 and Database secret engines.

## Features

- **Token-based Authentication**: Authenticate using a Vault token to retrieve secrets.
- **Interactive CLI**: Select secret types interactively and specify paths to retrieve specific data.
- **Supports KV v2 and Database Secret Engines**: Retrieve secrets stored in Vault’s KV or Database engines.
- **Error Handling**: Informative messages for authentication and other errors.

## Secret Engines Supported

- **Key/Value (KV) Version 2**: Access secrets in Vault’s KV store.
- **Database Secrets**: Fetch dynamic, time-limited database credentials.

## Installation

To install, ensure you have Python 3.6 or above, then use:

```bash
pip install vault_secrets
