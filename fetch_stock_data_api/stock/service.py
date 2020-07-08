import re

from requests import get

class StockService(object):

    @classmethod
    def fetch_data(cls, url=None):
        if url is None:
            raise AttributeError('url is null')

        resp = get(url)

        if resp.status_code == 200:
            return resp.content

    