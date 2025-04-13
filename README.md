# AnythingPassword
Password Management and Encryption Application
Overview
This Python application provides a suite of tools for generating, analyzing, encrypting, and managing passwords securely. It includes functionality to generate strong random passwords, evaluate password strength, calculate password entropy and crack time, check for password expiration, and detect common passwords. Additionally, it supports secure password encryption and decryption using the Fernet symmetric encryption algorithm, with the encryption key stored securely in the same directory as the script.

The application is designed to be modular, secure, and user-friendly, with robust error handling and platform compatibility (Unix-like systems and Windows).

Features
Password Generation:
Generates random passwords of specified length using a mix of lowercase, uppercase, digits, and special characters.
Default length is 8 characters if not specified.

Password Strength Analysis:
Evaluates passwords based on length, character types (uppercase, lowercase, digits, special characters), and commonality.
Provides feedback and a strong password suggestion if the input password is weak.
Checks against a list of common passwords.

Password Security Metrics:
Calculates password entropy (in bits) to measure randomness.
Estimates the time required to crack a password via brute force in seconds, minutes, or hours.
Checks if a password has expired based on a creation timestamp and maximum age (default 90 days).

Password Encryption/Decryption:
Encrypts passwords using a securely generated Fernet key.
Decrypts encrypted passwords using the same key.
Stores the encryption key securely in the script’s directory with restricted permissions.

Key Management:
Generates and saves a Fernet key to a file (encryption_key.key) in the script’s directory.
Loads the key from the file for encryption/decryption.
Ensures secure file permissions (owner-only read/write on Unix-like systems).

## Installation

```bash
pip install cryptography==44.0.2