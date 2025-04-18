from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask
from routes.home import home_bp
from routes.chat import chat_bp
from routes.health import health_bp
from routes.koan import koan_bp
from routes.magic import magic_bp
from routes.weather import weather_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(health_bp)
app.register_blueprint(koan_bp)
app.register_blueprint(magic_bp)
app.register_blueprint(weather_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)
