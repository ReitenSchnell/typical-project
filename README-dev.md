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
*Example*: `pylint so_parser`
* Generate code quality config `pylint --generate-rcfile > .pylintrc`

#####Unit tests
* Run tests in folder `python -m pytest [folder_path] -v`
*Example*: `python -m pytest .\tests -v`
* Run tests with coverage `python -m pytest [folder_path] -v --cov=[module_to_cover]`
*Example*: `python -m pytest .\tests -v --cov=so_parser`

#####Makefile
* To use it - install make http://gnuwin32.sourceforge.net/packages/make.htm
* To see possible commands: `make help`
* Running just `make` will call first command in the file

#####Virtual environment
* Install virtualenv `pip install virtualenv`
* Create virtual env `virtualenv venv`
* Activate virtual env `venv\Scripts\activate`
* Deactivate virtual env 'venv\Scripts\deactivate`

#####Uwsgi
* Start with parameters for nginx `uwsgi --socket 127.0.0.1:8080 --plugins=python34 --chdir=/work --file=app.py &`
* Start with ini file `uwsgi --ini /work/uwsgi.ini &`

#####Nginx
* Test config `service nginx configtest`
* Restart `service nginx restart`

#####Docker
* Current IP address `docker-machine ip`
* Go into console of running container `docker exec -it <container_id> /bin/bash`
* Building an image: `docker build -t <name:version> <path to docker file>`
*Example*: `docker build -t pywebdeb dockerfile.os`
* Creating container based on image: `docker run -it -p 8080:8080 -p 80:80 -v /$(pwd)/work:/work --name deb pywebdeb`
* Get container logs: `docker logs -f <container_name>`
* Get exit code of container: `docker wait <container_name>`
* Starting docker-compose: `docker-compose up -d -p <project_name>`
* Stopping docker-compose and removing containers: `docker-compose down`


#####Package distribution
* From the root folder of the project `python setup.py sdist`

