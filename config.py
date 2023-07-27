import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.urandom(32)

# Prefix of all routes
APPLICATION_ROOT = '/api'

# OpenAI API_KEY
OPENAI_APIKEY = os.environ.get("OPENAI_APIKEY", None)

# Grabs the folder where the script runs.
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Database detail
DATABASE = {
    'name': os.environ.get("DB_NAME", None),
    'user': os.environ.get("DB_USERNAME", None),
    'pass': os.environ.get("DB_PASSWORD", None),
    'host': os.environ.get("DB_HOST", None),
    'port': os.environ.get("DB_PORT", None),
}

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pass)s@%(host)s:%(port)s/%(name)s' % DATABASE

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False   

# Stripe Settings

STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", None)
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", None)