# 🔐 Rensomeware — File Encryption & Decryption

<p align="center">
  A Python-based educational file encryption and decryption project using Fernet symmetric encryption, with standalone Windows executable support.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Encryption-Fernet-green" alt="Encryption">
  <img src="https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-blue" alt="Platform">
  <img src="https://img.shields.io/badge/Purpose-Educational-orange" alt="Purpose">
</p>

## 📌 Overview

**Rensomeware** is a Python project that demonstrates file encryption and decryption using the Fernet symmetric encryption algorithm from the `cryptography` library.

The project contains two scripts:

- 🔒 `encrypted.py` — encrypts file contents.
- 🔓 `decrypted.py` — decrypts file contents.

Both scripts can be packaged into standalone Windows `.exe` files using PyInstaller.

> **Important:** Test this project only with disposable files in a dedicated test folder. Do not run it against an entire drive or files belonging to other people.

## ✨ Features

- 🔐 Fernet symmetric encryption and decryption.
- 📄 Support for text and binary file contents.
- 🪟 Windows 10 and Windows 11 support.
- 📦 Standalone Windows executable generation.
- ⚙️ SHA-256-based key derivation.
- 🐍 Python implementation.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Cryptography | Fernet encryption and decryption |
| Hashlib | SHA-256 hashing |
| Base64 | Key encoding |
| PyInstaller | Windows executable generation |

## 📂 Project Structure

```text
rensomeware/
├── encrypted.py
├── decrypted.py
├── requirements.txt
└── README.md
```

After building the executables, PyInstaller creates `build/` and `dist/` directories:

```text
rensomeware/
├── build/
└── dist/
    ├── encrypted.exe
    └── decrypted.exe
```

These generated directories are normally excluded from Git unless you intentionally want to publish the build artifacts.

## 🪟 Windows Installation (Windows 10/11)

### 1. Open the project directory

Open Command Prompt and run:

```cmd
cd /d C:\Users\ASUS\OneDrive\Desktop\rensomeware
```

### 2. Create a virtual environment

```cmd
py -m venv .venv
```

Activate it:

```cmd
.venv\Scripts\activate
```

### 3. Install dependencies

Make sure `requirements.txt` contains the packages required by this project:

```text
cryptography
pyinstaller
```

Install them:

```cmd
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

### 4. Run the Python scripts

Run the encryption script:

```cmd
py encrypted.py
```

Run the decryption script:

```cmd
py decrypted.py
```

Use disposable test files and confirm that your scripts handle the input and output paths as expected before testing further.

## 📦 Build Windows Executables

### 1. Install PyInstaller

If you installed the dependencies above, PyInstaller should already be available. Otherwise, run:

```cmd
py -m pip install pyinstaller
```

### 2. Build `encrypted.exe`

```cmd
py -m PyInstaller --clean --onefile encrypted.py
```

### 3. Build `decrypted.exe`

```cmd
py -m PyInstaller --clean --onefile decrypted.py
```

### 4. Locate the executables

After successful builds, the executables should be in the `dist` directory:

```text
dist/
├── encrypted.exe
└── decrypted.exe
```

### 5. Run the executables

From the project directory:

```cmd
dist\encrypted.exe
```

```cmd
dist\decrypted.exe
```

Standalone executables generally do not require a separate Python installation, although compatibility and runtime requirements can vary.

## 🐧 Building Windows EXEs from Kali Linux

PyInstaller does not natively cross-compile Windows executables from Kali Linux.

For Windows executables, use one of these approaches:

- Build directly on Windows.
- Build inside a Windows virtual machine.
- Use a Windows-based CI runner.

Running PyInstaller on Kali normally creates Linux executables, not Windows `.exe` files.

## 🐛 Troubleshooting

| Error | Possible cause |
|---|---|
| `ModuleNotFoundError` | Required package is missing from the active Python environment |
| `InvalidToken` | Incorrect Fernet key, invalid encrypted data, or modified data |
| `PermissionError` | Insufficient permission to access a file |
| Executable fails to launch | Packaging issue, missing dependency, or compatibility problem |

### Fix missing dependencies

```cmd
py -m pip install -r requirements.txt
```

### Rebuild the executables

If you change the Python code, rebuild the corresponding executable:

```cmd
py -m PyInstaller --clean --onefile encrypted.py
py -m PyInstaller --clean --onefile decrypted.py
```

## 🔒 Security Notes

- Use only on files you own or are authorized to test.
- Use disposable test files and keep backups of important data.
- Never publish secret keys or passwords in a public repository.
- Use the same key-derivation method for encryption and decryption.
- Protect encryption keys: losing the correct key may make encrypted data unrecoverable.
- Keep testing confined to a dedicated test directory.

## 🎯 Learning Objectives

- Python file handling
- Symmetric encryption fundamentals
- Key derivation and management
- Exception handling
- Python dependency management
- Windows executable packaging with PyInstaller

---

<p align="center">
  <strong>Built with Python 🐍 | Educational Cybersecurity Project 🔐</strong>
</p>

