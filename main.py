from flask import Flask
from service.latest_news_service import LatestNewsService
app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_health():
    return {"response": "Ok"}


@app.route('/news/tech-latest', methods=["GET"])
def get_latest_tech_news():
    lns = LatestNewsService()
    data = lns.fetch_latest_news()
    return data


@app.route('/profile', methods=["GET"])
def get_profile():
    data = {"ok": "profile"}
    return data


if __name__ == "__main__":
    app.run(port=2051)
