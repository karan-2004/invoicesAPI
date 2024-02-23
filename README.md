# invoicesAPI
Invoices API created using django rest framework

# Steps for set-up
## Run the following commands in your terminal(lines starting with # are annotations not for execution)
> #Creating a directory for the application

`mkdir invoicesDir`
> #Creating environment(make sure you have python and pip installed)

`pip install venv`

`python -m venv environment`

> #activating environment

> #for windows

`environment/Scripts/activate`

>#for linux

`source environment/bin/activate`

>#Cloning the repository

`git clone https://github.com/karan-2004/invoicesAPI invoices -b main`

>#changing the directory

`cd invoices`

>#Installing dependencies

`pip install -r requirements.txt`

>#For database connectivity

`python manage.py makemigrations`

`python manage.py migrate`

# Now you are ready to run the application 
>#The final command

`python manage.py runserver`

## search `127.0.0.1:8000` in the browser
