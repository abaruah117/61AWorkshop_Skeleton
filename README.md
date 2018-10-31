# Setup Instructions
---
## Mac
1. Install [Brew](https://brew.sh/)
`$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
2. Install [pip](https://pip.pypa.io/)
```
$ [sudo] easy_install pip
$ pip --version
```
3. Install [virtualenv](https://virtualenv.pypa.io/en/latest/)
```
$ [sudo] pip install virtualenv
$ virtualenv --version
```
4. Set up your virtual environment
```
$ virtualenv env
$ source env/bin/activate
```
4. Install Flask (and the other dependencies)
`pip install -r requirements.txt`
5. Run the Flask server!
`$ python app.py`

## Windows
(TBD)