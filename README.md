# Template creator
A cli tool for creating basic flask apps
## Make sure you have a virtualenv activated
```
# if you don't have a virtualenv run
python -m venv VIRTUALENV name
or
python3 -m venv VIRTUALENV name
``` 
### How to use
run the command ```pip install Template-Creator```<br>
cd into the directory where you want to create a project then run 
```python
python -m template_creator
```
the available options are 
```python
# create a template with bootstrap enabled
python -m template_creator --template=bootstrap
```
```python
# create a template with w3css enabled
python -m template_creator --template=w3css
```
```python
# create a template with no css framework enabled
python -m template_creator
```