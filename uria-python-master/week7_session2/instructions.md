Python, VSCode, and NLTK setup
==============================

[Python 3.8.3 download](https://www.python.org/downloads/release/python-383/)

[Visual Studio Code download](https://code.visualstudio.com/)

---
When installing Python, make sure that the `☑ Add Python 3.8 to Path` option is selected.

---
### Windows:
Open either **Command Prompt**/**Simbolo de Sistema** or **Powershell**.
### Mac/Linux:
Open **Terminal**.

---
The Windows version of these commands will be printed first, with Mac/Linux appropriate versions afterwards.

Run the command:
```
Windows:      pip --version
Mac/Linux:    pip3 --version
```
or:
```
Windows:      python --version
Mac/Linux:    python3 --version
```
to check Python has installed correctly and has been added to the Path.

If successful, we need to install the module **nltk** with *one* of the following:
```
Windows:      pip install nltk
Mac/Linux:    pip3 install nltk

Windows:      python -m install nltk
Mac/Linux:    python3 -m pip install nltk
```
Finally, run Python in an interactive shell with:
```
Windows:      python
Mac/Linux:    python3
```
and open the nltk downloader:
```
All OSs:       import nltk
               nltk.download()
```
![nltk.download()](https://github.com/tt-n-walters/uria-python/raw/master/week7_session2/nltkdownloader.png)

Select `all` in *Collections*->*Identifier* and click `Download`.