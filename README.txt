0. Check python version
python -V
1. Installing requirements
pip install -r [file-name]
Example: pip install -r requirements.txt
1.1 Saving requirements
pip freeze >[file-name]
Example: pip freeze >requirements.txt
2. Check version of a package
pip show <package-name>
Example: pip show requests
3. Run code quality check
pylint .\so_client\client.py
3.1 Generate code quality config
pylint --generate-rcfile > .pylintrc
4. Run tests in folder
python -m pytest [folder_path] -v
Example: python -m pytest .\tests -v
5. Run tests with coverage
python -m pytest [folder_path] -v --cov=[module_to_cover]
Example: python -m pytest .\tests -v --cov=so_client


