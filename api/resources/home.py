import falcon
import json
import os
import requests

from decimal import Decimal
from datetime import datetime


class Home:
    
    def __init__(self):
        pass

    def on_get(self, req, res, category_sub_code=None, due_code=None):
        res.status = falcon.get_http_status(status_code=200)
        response = requests.request("GET", "http://www.mocky.io/v2/5e7beacf2d0000979811aa3e")
        print("Recebido GET em {}".format(datetime.utcnow().isoformat()))
        response = json.loads(response.text)
        res.body = json.dumps(response)

    def on_post(self, req, res):
        body = req.stream.read(req.content_length or 0)
        body = json.loads(body.decode('utf-8'), parse_float=Decimal)
        print("Recebido POST em {}".format(datetime.utcnow().isoformat()))
        res.status = falcon.get_http_status(status_code=200)
        response_dict = {
            "company": "qi_tech",
            "proccess_id": str(os.getpid()),
            "body": body
        }
        res.body = json.dumps(response_dict)
