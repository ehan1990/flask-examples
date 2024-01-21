
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
@click.option('--limit', required=False, default=5)
@click.option('--page', required=False, default=1)
def show_urls(limit, page):
    api_url = f"{constants.LOCALHOST_ROOT}/urls?limit={limit}&page={page}"
    res = call_api(api_url, "GET")
    print(json.dumps(res, indent=2))
