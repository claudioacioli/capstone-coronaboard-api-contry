import os
import sys

from app import create_app, db
from app.models import Country
from flask_migrate import Migrate

app = create_app('dev')
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
