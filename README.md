# EventManager

# very raw db scheme
"has" has to be intended as the direction of the foreign key, for example:
if A-(0,N)-B then B has a foreign key versus A inside the database
https://shorturl.at/awBR5

## Install

### Setup db
postgres or mysql
https://docs.djangoproject.com/en/3.2/ref/settings/#databases
https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DATABASE-ENGINE
do not push your settings, write and import your local own from remote.py instead
this file is listed in gitignore

database steps (postgres):

    create database dbname;
    create user dbuser;
    alter user dbuser with login;
    alter user dbuser with password 'dbuserpass';
    grant all privileges on database dbname to dbuser;
    \q

### Setup Django    
create a folder, open it, git clone this project and make a virtual environment 

pip3 install -r requirements.txt

### Start project
you will need to do initial migrations

    python3 manage.py makemigrations
    python3 manage.py migrate

then create a super user

    python3 manage.py createsuperuser

now you can run

    python3 manage.py runserver
   
django admin panel: http://127.0.0.1/admin 

