import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def pig_latin_translation():

    fact = get_fact()
    payload = {"input_text": fact}
    latin_response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", data=payload)

    return latin_response.url


@app.route('/')
def home():
    url = pig_latin_translation()
    return url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='172.16.68.3', port=port)
