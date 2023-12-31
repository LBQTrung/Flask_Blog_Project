import os
from app import create_app, db
from app.models import User
from flask_migrate import Migrate

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True, port=5000, host="0.0.0.0")
