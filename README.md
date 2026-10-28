# 🔐 Rensomeware — File Encryption & Decryption

<p align="center">
  An educational Python project demonstrating Fernet symmetric file encryption and decryption, with standalone Windows executable support.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Encryption-Fernet-green" alt="Encryption">
  <img src="https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-blue" alt="Platform">
  <img src="https://img.shields.io/badge/Purpose-Educational-orange" alt="Purpose">
</p>

---

## 📌 Overview

**Rensomeware** is a Python project that demonstrates file encryption and decryption using the Fernet symmetric encryption algorithm provided by the `cryptography` library.

The project contains two Python scripts:

- 🔒 `encrypted.py` — demonstrates file encryption.
- 🔓 `decrypted.py` — demonstrates file decryption.

PyInstaller can package the scripts into standalone Windows executables.

## ✨ Features

- 🔐 Fernet symmetric encryption and decryption
- 📄 Support for text and binary file contents
- 🪟 Windows 10 and Windows 11 support
- 📦 Standalone Windows executable generation
- ⚙️ SHA-256-based key derivation
- 🐍 Python implementation
- 📋 Dependency management through `requirements.txt`

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Cryptography | Fernet encryption and decryption |
| Hashlib | SHA-256 hashing |
| Base64 | Key encoding |
| PyInstaller | Windows executable generation |
| Git | Source code management |

## 📂 Project Structure

```text
Rensomeware/
│
├── encrypted.py       # File encryption script
├── decrypted.py       # File decryption script
├── requirements.txt   # Required Python packages
├── README.md          # Project documentation
│

```

### 📁 File and Directory Description

| File / Directory | Description |
|---|---|
| `encrypted.py` | Python encryption script |
| `decrypted.py` | Python decryption script |
| `requirements.txt` | Lists the required Python packages |
| `README.md` | Project documentation |


**Note:** The `.venv/`, `build/`, and `dist/` directories are normally created locally and may not be included in the GitHub repository. The `.exe` files appear after successfully building the scripts on Windows.

## 📥 Installation

### Requirements

Before installing, make sure you have:

- Windows 10 or Windows 11
- Python 3 installed
- Git installed if you want to clone the repository

### Method 1: Clone the Repository

**Step 1 — Open Command Prompt**

**Step 2 — Download the project**

```cmd
git clone https://github.com/shahid680/Ransomware.git
```

**Step 3 — Open the project directory**

```cmd
cd Ransomware
```

### Method 2: Download ZIP

1. Visit the [Rensomeware GitHub repository](https://github.com/shahid680/Ransomware).
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the downloaded ZIP file.
5. Open Command Prompt in the extracted project directory.

## ⚙️ Set Up the Environment

### Step 1 — Create a virtual environment

```cmd
py -m venv .venv
```

### Step 2 — Activate the environment

```cmd
.venv\Scripts\activate
```

### Step 3 — Install dependencies

The `requirements.txt` file should list the packages required by the project, for example:

```text
cryptography
pyinstaller
```

Install the packages using:

```cmd
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

If the `py` command is unavailable, check that Python is installed and added to your system's PATH.

## ▶️ Run the Python Scripts

Run the encryption script:

```cmd
py encrypted.py
```

Run the decryption script:

```cmd
py decrypted.py
```

Before testing, check the paths configured in your scripts. Use only disposable test files in a dedicated test directory and verify the results before proceeding.

## 📦 Build Windows Executables

You can package the Python scripts into Windows executables using PyInstaller.

### Step 1 — Build `encrypted.exe`

```cmd
py -m PyInstaller --clean --onefile encrypted.py
```

### Step 2 — Build `decrypted.exe`

```cmd
py -m PyInstaller --clean --onefile decrypted.py
```

### Step 3 — Locate the executables

After successful builds, the generated files should be in the `dist` directory:

```text
dist/
├── encrypted.exe
└── decrypted.exe
```

### Step 4 — Run the executables

Run the encryption executable:

```cmd
dist\encrypted.exe
```

Run the decryption executable:

```cmd
dist\decrypted.exe
```

PyInstaller bundles the Python interpreter and required dependencies for typical standalone use. Build compatibility can depend on the target Windows environment.

## 🐧 Building Windows EXEs from Kali Linux

PyInstaller does not natively cross-compile Windows executables from Kali Linux.

To generate Windows `.exe` files, use one of these options:

- Build directly on a Windows computer.
- Build inside a Windows virtual machine.
- Use a Windows-based CI runner.

Running PyInstaller on Kali Linux normally creates Linux executables rather than Windows `.exe` files.

## 🐛 Troubleshooting

| Error | Possible cause |
|---|---|
| `ModuleNotFoundError` | A required Python package is missing |
| `InvalidToken` | Incorrect Fernet key or invalid encrypted data |
| `PermissionError` | Insufficient permission to access a file |
| `py is not recognized` | Python launcher is unavailable or not on PATH |
| Executable fails to launch | Packaging issue or environment compatibility problem |

### Reinstall dependencies

```cmd
py -m pip install -r requirements.txt
```

### Rebuild the executables

If you modify the Python source files, rebuild the corresponding executables:

```cmd
py -m PyInstaller --clean --onefile encrypted.py
py -m PyInstaller --clean --onefile decrypted.py
```

## 🔒 Security Notes

- Use the project only on files you own or are authorized to test.
- Use disposable files in an isolated test directory.
- Keep backups of important data.
- Never publish secret keys or passwords in a public repository.
- Use the same key-derivation method for encryption and decryption.
- Protect your encryption key because losing the correct key may make encrypted data unrecoverable.
- Review the file paths used by the scripts before running them.

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
