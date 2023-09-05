import requests
import re
import pandas as pd


def get_dp_from_amazon_links(link):
    pattern = r'/dp/(\w+)/'
    match = re.search(pattern, link)
    if match:
        dp = match.group(1)
        return dp


def get_product_detail(path, col_name):
    df = pd.read_excel(path)
    column = df[col_name]

    for link in column:
        product_dp = get_dp_from_amazon_links(link)
        if product_dp is not None:
            payload = {'api_key': '254d841e6c10f3169652c1e73a2133e7',
                       'asin': product_dp, 'country': 'ae', 'tld': 'ae'}
            r = requests.get('https://api.scraperapi.com/structured/amazon/product', params=payload)
            print(r.text)
        else:
            print("This link doesn't match structure", link)
            pass
