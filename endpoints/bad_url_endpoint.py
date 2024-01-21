from flask import Blueprint, request, jsonify
from libs.mongo_service import MongoService
from util import constants

bad_url_blueprint = Blueprint("badurl", __name__)


def check_if_bad_url_exists(url: str):
    search = {"url": url}
    res = MongoService.query_one(constants.COL_BAD_URL, search)
    if res is None:
        return False
    return True


def get_all_bad_urls():
    res = MongoService.query(constants.COL_BAD_URL)
    return res


def add_one_bad_url(url_data: dict):
    MongoService.insert(constants.COL_BAD_URL, url_data)


def delete_one_bad_url(url: str):
    q = {"url": url}
    MongoService.delete_one(constants.COL_BAD_URL, q)


@bad_url_blueprint.route("/badurl/check", methods=["GET"])
def check_bad_url_endpoint():
    url = request.args.get("url")
    exists = check_if_bad_url_exists(url)
    res = {"url": url, "exists": exists}
    return jsonify(res)


@bad_url_blueprint.route("/badurl/urls", methods=["GET", "POST"])
def add_ls_url_endpoint():
    if request.method == "POST":
        req = request.get_json(force=True)
        add_one_bad_url(req)
        url = req.get("url")
        res = {"msg": f"added {url}"}
        return jsonify(res)
    elif request.method == "GET":
        res = get_all_bad_urls()
        return jsonify(res)


@bad_url_blueprint.route("/badurl/urls/<url>", methods=["DELETE"])
def delete_url_endpoint(url: str):
    delete_one_bad_url(url)
    res = {"msg": f"deleted {url}"}
    return jsonify(res)
