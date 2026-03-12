## Overview 
![alt text](<./screenshots/Screenshot from 2026-03-11 13-37-07.png>)

![alt text](<./screenshots/Screenshot from 2026-03-11 13-38-59.png>)

![alt text](<./screenshots/Screenshot from 2026-03-11 13-45-48.png>)

## Disclaimer
The ```venv/bin/activate``` is configured mainly for fish. If you face issues with activating the virtual environment using bash then you're suggested to use fish(friendly interactive shell). Or you can continue with the bash by changing these two lines: ![alt text](./screenshots/image.png) Replace them with 
```
_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/"bin":$PATH"
```
## 📋 Prerequisites
- Python 3 or higher installed on your system
- Git (to clone the repository)
- Basic command line knowledge

## 🚀 Quick Start Guide
Clone this repo in your local machine and activate the python virtuan environment.
### Windows (Command Prompt):
```bash
venv\Scripts\activate
```
### For macOS/Linux
```bash
source venv/bin/activate
```

### You need to install packages 
```bash
pip install cryptography zxcvbn bcrypt
```
### To Deactivate (if activated first)
```bash
deactivate
```

## Delete the venv folder
How to delete this virtual environment from your machine
### For Windows:
```bash
rmdir /s venv
```
### For macOS/Linux:
```bash
rm -rf venv
```
