from os import getenv

from dotenv import load_dotenv

load_dotenv(override=True)
ACCESS_TOKEN = getenv("ACCESS_TOKEN")
USER = getenv("USER")
PWD = getenv("PWD")
DATABASE_URL = getenv("DATABASE_URL")
API_URL = getenv("API_URL")

ENV = getenv("ENV")
if ENV == 'development':
    DATABASE_URL = "mysql+aiomysql://neves:12qwaszx@localhost:3306/casamento"
    API_URL = "http://localhost:8000"
