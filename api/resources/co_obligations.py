import falcon
import json
import os
import requests

from datetime import datetime
from utils import Operations

operation = Operations()

class CoObrigations:

    def __init__(self):
        self.category_code = 15
        self.operation_items = []
        self.operation_category_sub_code = []
        self.operation_due_code = []

    def on_get(self, req, res, category_sub_code=None, due_code=None):
        res.status = falcon.get_http_status(status_code=200)
        response = requests.request("GET", "http://www.mocky.io/v2/5e7beacf2d0000979811aa3e")
        print("CoObrigations - Recebido GET em {}".format(datetime.utcnow().isoformat()))
        response = json.loads(response.text)
        response["risk_rank"] = operation.risk_rank(response=response)
        response["operation_items"] = operation.category_code(
            response=response,
            category_code=self.category_code,
            operation_items=self.operation_items
        )
        if category_sub_code:
            # 1 
            if self.operation_category_sub_code:
                self.operation_category_sub_code = []
            self.operation_items = operation.category_sub_code(
                response=response,
                operation_category_sub_code=self.operation_category_sub_code,
                category_sub_code=str(category_sub_code)
            )
        # busca por código de vencimento
        if due_code:
            # 120, 130, 140, 150, 165
            if self.operation_due_code:
                self.operation_due_code = []
            self.operation_items = operation.due_code(
                response=response,
                operation_due_code=self.operation_due_code,
                due_code=due_code
            )
        response["operation_items"] = self.operation_items
        res.body = json.dumps(response)
