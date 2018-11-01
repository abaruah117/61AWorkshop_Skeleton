# Setup Instructions

## Mac
1. **Install [Brew](https://brew.sh/)** (if not already installed)
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. **Install [pip](https://pip.pypa.io/)** (if not already installed)
```
$ [sudo] easy_install pip
$ pip --version
```

3. **Install [virtualenv](https://virtualenv.pypa.io/en/latest/)** (if not already installed)
```
$ [sudo] pip install virtualenv
$ virtualenv --version
```

4. **Set up your virtual environment**
```
$ virtualenv env
$ source env/bin/activate
```

4. **Install Flask (and the other dependencies)**
```
pip install -r requirements.txt
```
5. **Run the Flask server!**
```
$ python app.py
```

## Windows
0. You should already have python3 and pip installed from the first CS61A lab. To confirm that you have pip run `pip -V` and make sure it outputs something like pip `9.0.1 from...` (it's okay if the version number is a little different).

1. **Open git bash and navigate to this directory**

2. **Create a virtual environment**
```
$ python -m venv env
```
If you normally use py or python3 instead of python to run python files use that instead.

3. **Activate the virtual environment**
```
$ source env/Scripts/activate
```
You will have to do this every time you open a new terminal.

4. **Install Flask (and the other dependencies)**
```
$ pip install -r requirements.txt
```

5. **Run the Flask server!**
```
$ python app.py
```
