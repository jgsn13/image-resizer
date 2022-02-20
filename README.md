# Image Resizer
- Pip dependencies: pyside6, pyinstaller.
### Change the UI
- Use Qt Designer 6 to open the **design.ui** file and make some changes.
- Recompiling the UI:
```sh
pyside6-uic design.ui -o design.py
```
### Building
- A binary file with **<name>** will be generated in **dist/** folder.
```sh
pyinstaller --name="<name>" --windowed --onefile main.py
```
### Troubleshooting
- Python library not found error:
  1. Use [pyenv](https://github.com/pyenv/pyenv) to reinstall python.
  2. Reinstall python:
  ```
  env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.8.0
  ```
