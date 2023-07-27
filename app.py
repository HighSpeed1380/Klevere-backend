from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

import config
from models import db
from api.auth import auth_bp
from api.chatgpt import chatgpt_bp
from api.stripe import stripe_test

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config.from_object(config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(chatgpt_bp, url_prefix='/api/gpt')
app.register_blueprint(stripe_test, url_prefix='/api/stripe')


if __name__ == "__main__":
    app.run(debug=True)