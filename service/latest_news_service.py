from scrapper.latest_news_scrapper import LatestNewsScrapper


class LatestNewsService:

    def fetch_latest_news(self):
        latest_ns = LatestNewsScrapper()
        data = latest_ns.execute()
        data = self.process_response(data)
        return data

    @staticmethod
    def process_response(data):
        data = {"latest-posts": data}
        return data
