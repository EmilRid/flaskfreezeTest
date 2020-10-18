from flask_frozen import Freezer
from run import app
import os

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
