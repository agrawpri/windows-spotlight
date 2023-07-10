![Docker Image Size (tag)](https://img.shields.io/docker/image-size/agrawpri/windows-spotlight/latest)

# windows-spotlight
A simple utility to find and copy Windows spotlight images on your Windows PC to your preferred destination so that they
can be used as wallpapers and such.

## Run as a windows executable
### Prerequisites
**OS**: Windows   
**Packages**: git, python3, pip

### Steps
In a Windows powershell or command prompt, run the following:
1. `git clone https://github.com/agrawpri/windows-spotlight`
2. `cd windows-spotlight`
3. `python3 -m pip install -r requirements.txt`
4. `python3 -m pip install pyinstaller`
5. `$env:path += ';C:\Users\Admin\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts;'`
6. `pyinstaller.exe --onefile --windowed driver.py`

This should generate a `./dist/main.exe`. Just run (double-click) this file, and it should copy all the spotlight images
to `C:\Users\Admin\Pictures\Spotlight`. Rerun once every day to copy new images downloaded that day.

## Run as a docker container
### Prerequisites
**OS**: Windows(10+)  
**Installations**: Docker desktop, git

### Steps
In a Windows powershell or command prompt, run the following:
1. `git clone https://github.com/agrawpri/windows-spotlight`
2. `cd windows-spotlight`
3. `docker-compose run --rm windows-spotlight`

Rerun step #3 once every day to copy new images downloaded that day to `C:\Users\Admin\Pictures\Spotlight`. That's it! 

Notice how using docker simplifies the workflow so much. This is because of the following reasons:
- You don't need to have python3/pip pre-installed. Instead, we can just use a docker image which has those installed.
- You don't manually need to install python requirements (pip install) since the Dockerfile already knows to do that.
- You don't need to use something like `pyinstaller` to build a Windows executable out of this source code. Windows (10+)
natively supports running linux based docker containers.
