# Igor
Igor is a question and answer site where users can sign up and choose a specialty.  After they sign up they have the ability to ask questions to any specialty and answer any questions within their specialty.

## Dependencies
```
pip install django==2.2
pip install bcrypt
```
## Install Instructions

1. Clone the repository
```
git clone https://github.com/dylanPMurphy/Igor
```
2. cd into the Igor folder
```
cd Igor
```
3.Create a new virtual environment
 ```
python 3 -m venv venv
 ```
4.Run Virtual Evironment
 ```
source venv/bin/activate 
 ```
5.cd into igor folder
```
cd igor
``` 
6.Make migrations & migrate
```
python manage.py makemigrations
python manage.py migrate
```
7.Runserver
```
python manage.py runserver
```
