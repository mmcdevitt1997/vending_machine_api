# Vending Machine API

## Instructions

These are instructions on how to get the Vending Machine API up and run as that you make to call the API.

### Requirements
Make sure you have Python 3.7 or greater installed and are able to use pip.

### Installing Process

Clone this repository down in desired location:

```
git@github.com:mmcdevitt1997/vending_machine_api.git
```

Create your virtual environment

```
cd vending_machine_api
python -m venv VendingEnv
source ./VendingEnv/bin/activate
```

Download all the requirements using pip

```
pip install -r requirements.txt
```


Run the migrations

```
python manage.py makemigrations vendingapp
python manage.py migrate
```

Then load some starting data.

```
python manage.py loaddata vending_machine
```

Finally run the server.

```
python manage.py runserver
```
The Vending Machine API is now up and running you can use Postman to test the API.

Here is a list of calls you can make with this API.

![HTTP chart](/images/HTTP.png)

