
import click
import json
import requests

from util import constants


def call_api(url, method, data=None):
    res = None
    if method == "GET":
        res = requests.get(url)
    elif method == "POST":
        res = requests.post(url, json=data)
    elif method == "DELETE":
        res = requests.delete(url)
    return res.json()


@click.group(name="url")
def url_cmd():
    pass


@url_cmd.command(name="add")
@click.option('--url', required=True)
def add_url(url: str):
    api_url = f"{constants.LOCALHOST_ROOT}/urls"
    data = {"url": url}
    res = call_api(api_url, "POST", data)
    print(json.dumps(res, indent=2))


@url_cmd.command(name="delete")
@click.option('--url', required=True)
def delete_url(url: str):
    api_url = f"{constants.LOCALHOST_ROOT}/urls/{url}"
    res = call_api(api_url, "DELETE")
    print(json.dumps(res, indent=2))


@url_cmd.command(name="ls")
def show_urls():
    api_url = f"{constants.LOCALHOST_ROOT}/urls"
    res = call_api(api_url, "GET")
    print(json.dumps(res, indent=2))

#
# @stock_cmd.command(name="add-sp500")
# @click.option('--count', "count", default=1)
# def add_sp500(count):
#     with open("data/sp500.json") as f:
#         data = json.loads(f.read())
#
#     if not count:
#         count = len(data)
#     count = int(count)
#
#     for i, d in enumerate(data):
#         if i == count:
#             break
#         ticker = d["ticker"]
#         print(f"{i+1}: inserting {ticker}")
#         stock_db = stock_service.get_one_stock_from_api(ticker)
#         MongoService.upsert(COL_STOCKS, stock_db.ticker, stock_db.__dict__)
#
#     print(f"inserted {count} stocks")
#
#
# @stock_cmd.command(name="ls")
# def show_all_stocks():
#     data = MongoService.get_all(COL_STOCKS)
#     print(json.dumps(data, indent=2))
#
#
# @stock_cmd.command(name="del")
# @click.option('--ticker', required=True)
# def del_stock(ticker):
#     stock_service.delete_one_stock(ticker)
#
#
# @stock_cmd.command(name="delall")
# def del_all_stock():
#     stocks = MongoService.get_all(COL_STOCKS)
#     for stock in stocks:
#         ticker = stock.get("ticker")
#         stock_service.delete_one_stock(ticker)
