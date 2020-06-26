Follow the following steps for set up:

# Introduction

# Developer Guide

## Getting Started

### Prerequisites
- [python3.0+](https://www.python.org/downloads/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)


### Install prerequisites

#### Python3.0+

Upgrade python to python3+ and make it as the default python


Now, get inside the program directory and create virtualenv as follows:

```
virtualenv -p python3 venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

Install the requirements as:

```
pip install -r requirement.txt
```

Run the following commands to migrate the data in db:

```
python3 manage.py migrate
python3 manage.py populate
```

python3 manage.py migrate : This command will create the table in the default mysql database.

python3 manage.py populate: The custom management command which will auto populate the table with some default values.

To finally run the program in local:
```
python3 manage.py runserver
```

API to get the user activity details
```
http://localhost:8000/activity/tracker/detail/
```
This is the GET request.


You can als view the hosted API by hitting the below mentioned link:
```
http://ec2-15-206-125-204.ap-south-1.compute.amazonaws.com/activity/tracker/detail/
```
