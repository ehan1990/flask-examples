import datetime
import logging
from flask import Flask, jsonify

from endpoints.bad_url_endpoint import bad_url_blueprint
from libs.mongo_service import MongoService
from util.constants import BAD_URL_DB_NAME

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(filename)s:%(lineno)d %(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

VERSION = "1.0.0"


app = Flask(__name__)
app.register_blueprint(bad_url_blueprint)


@app.route("/healthcheck", methods=["GET"])
def healthcheck_endpoint():
    data = {
        "msg": f"Running version {VERSION}",
        "date": f"{datetime.datetime.utcnow().isoformat()[0:19]}Z",
    }
    return jsonify(data)


def main():
    MongoService.init(BAD_URL_DB_NAME)
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)


if __name__ == "__main__":
    main()
