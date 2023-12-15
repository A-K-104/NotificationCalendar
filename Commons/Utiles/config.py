from flask import Flask
from sqlalchemy.orm import declarative_base

app = Flask(__name__)
Base = declarative_base()
