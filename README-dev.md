#Project commands
#####Check python version
`python -V`

#####Project Requirements
* Installing requirements `pip install -r [file-name]`
*Example*: `pip install -r requirements.txt`
* Saving requirements  `pip freeze >[file-name]`
*Example*: `pip freeze >requirements.txt`

#####Package manager
* Check package version `pip show <package-name>`
*Example*: `pip show requests`

#####Code quality 
* Check `pylint [package_name]`
*Example*: `pylint so_client`
* Generate code quality config `pylint --generate-rcfile > .pylintrc`

#####Unit tests
* Run tests in folder `python -m pytest [folder_path] -v`
*Example*: `python -m pytest .\tests -v`
* Run tests with coverage `python -m pytest [folder_path] -v --cov=[module_to_cover]`
*Example*: `python -m pytest .\tests -v --cov=so_client`

#####Makefile
* To use it - install make http://gnuwin32.sourceforge.net/packages/make.htm
* To see possible commands: `make help`

#####Virtual environment
* Install virtualenv `pip install virtualenv`
* Create virtual env `virtualenv venv`
* Activate virtual env `venv\Scripts\activate`
* Deactivate virtual env 'venv\Scripts\deactivate`

