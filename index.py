from app import app
from Databases.db import landingdb

with app.app_context():
    landingdb.create_all()

if __name__ == "__main__":
    app.run(debug=True)
