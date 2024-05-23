import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

configuration = {
    "AWS_ACCESS_KEY": ACCESS_KEY,
    "AWS_SECRET_KEY": SECRET_KEY,
}

