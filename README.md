# Klevere Backend

- Integrated ChatGPT API for Chat bot
- Flask MVC Pattern
- PostgreSQL ORM
- Authentication with JWT token

## Installation

### Set up Python Environment

- Install Python [here](https://www.python.org/downloads/)
- Set up Python Virtual Environment and Activate

```cli
python -m venv venv
```

```cli
.\venv\Scripts\activate
source ./venv/Scripts/activate
```

- Install required Libraries

```cli
pip install -r requirements.txt
```

### Set up PostgreSQL Database Environment

- Install PostgreSQL [here](https://www.postgresql.org/download/) (Remember Username, Password, Port)

### Set Environment Variables

- .env

| Variable      | Explanation                     |
| ------------- | ------------------------------- |
| OPENAI_APIKEY | Your OpenAI API Key for ChatGPT |
| DB_NAME       | Database Name                   |
| DB_PASSWORD   | Database Password               |
| DB_USERNAME   | Database Username               |
| DB_HOST       | Database Server Host            |
| DB_PORT       | Database Server Port            |

If server does not run, you can do it

- initdb -D "C:\PostgreSql\15\data" -U postgres

- pg_ctl start -D "C:\PostgreSql\15\data"

- pg_ctl register -N PostgreSql-12.3.1 -D "C:\PostgreSql\15\data"

If you need to use another Database server, then change SQLALCHEMY_DATABASE_URI variable in config.py to yours.

- .flaskenv

| Variable              | Explanation                                  |
| --------------------- | -------------------------------------------- |
| FLASK_APP             | Flask application                            |
| FLASK_ENV             | Running Mode                                 |
| FLASK_DEBUG           | Enable Debugging mode                        |
| FLASK_RUN_EXTRA_FILES | Don't Restart application when files changed |
| FLASK_RUN_HOST        | Host IP address                              |
| FLASK_RUN_PORT        | Port                                         |

### Initial Database Migration

```cli
flask db init
```

```cli
flask db migrate
```

```cli
flask db upgrade
```

### Run Server

```cli
flask run
```

### Get all modules

pip freeze > requirements.txt
