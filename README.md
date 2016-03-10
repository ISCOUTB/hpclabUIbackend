# hpclab-ui-backend

## Required for local test

- Python 2.7
- MySQL

## Packages to install (Ubuntu 14.04)

```
 sudo apt install -y python-dev libldap2-dev libsasl2-dev libssl-dev libmysqlclient-dev python-pip python-virtualenv
```

## Executing the project

First, create the virtualenv

```
 virtualenv hpclabapi
```
Activate it

```
 source hpclabapi/bin/activate
```
Once it's activated, clone the repository and install all required packages described on requirements.txt file.

```
 git clone https://github.com/IngenieriaDeSistemasUTB/hpclabUIbackend.git
 cd hpclabUIbackend/
 pip install -r requirements.txt
```
Before continue it's neccesary a MySQL database called 'hpclabapi'
```
 mysql -u root -p
 create database hpclabapi;
 exit
```
Run the migrations
```
 ./manage.py migrate
 ./manage.py makemigrations hpcuiapi
 ./manage.py migrate hpcuiapi
```
Then, run the server
```
./manage.py runserver 0.0.0.0:9000
```
