# Vending Machine API

## Getting Started
Make sure you have Python 3.7 or greater installed.


Clone this repository down in desired location:

```
git@github.com:mmcdevitt1997/vending_machine_api.git
```

Enter these commands:

```
cd vending_machine_api
python -m venv VendingEnv
source ./VendingEnv/bin/activate
```
Then load some starter data

```
python manage.py loaddata vending_machine
```


Then migrate the data

```
python manage.py makemigrations vendingapp
python manage.py migrate
```


Run

```
python manage.py runserver
```
The Vending Machine API is now up and running you can Postman or any other serves using HTTP calls.

Here is a list call you can make with this API. 

![HTTP chart](/Desktop/HTTP.png)

