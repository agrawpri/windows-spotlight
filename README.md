# windows-spotlight
A simple utility to find and copy Windows spotlight images on your Windows PC to your preferred destination so that they can be used as wallpapers and such.

## Build
### Prerequisites
**OS**: Windows   
**Packages**: git, python3, pip

### Steps
In a Windows powershell or command prompt, run the following:
1. `git clone https://github.com/agrawpri/windows-spotlight`
2. `cd windows-spotlight`
3. `python3 -m pip install -r requirements.txt`
4. `$env:path += ';C:\Users\Admin\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts;'`
5. `pyinstaller.exe --onefile --windowed main.py`

This should generate a `./dist/main.exe`. Just run (double-click) this file, and it should copy all the spotlight images
to `C:\Users\Admin\Pictures\Spotlight`. Rerun once every day to copy new images downloaded that day.
