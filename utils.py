
from constants import RiskRankConstants

rr_constants = RiskRankConstants()

class Operations:

    def risk_rank(self, response):
        # Creio eu que o pedido de cálculo de confiável e não confiável é por esse caminho
        credit_wallet = 0.0
        risk_total = 0.0
        for i in range(0, len(response["operation_items"])):
            if response["operation_items"][i]["due_type"]["due_type_group"] in rr_constants.CREDIT_WALLET_DUE_TYPE_GROUP:
                credit_wallet += response["operation_items"][i]["due_value"]
            elif response["operation_items"][i]["due_type"]["due_type_group"] in rr_constants.RISK_TOTAL_DUE_TYPE_GROUP:
                risk_total += response["operation_items"][i]["due_value"]
        risk_total += credit_wallet
        total = (credit_wallet / risk_total)
        total = round(total, 2)
        if total >= 0.00 and total < 25.00:
            risk_type = rr_constants.RISK_TYPES[0]
        elif total >= 25.00 and total < 50.00:
            risk_type = rr_constants.RISK_TYPES[1]
        elif total >= 50.00 and total < 75.00:
            risk_type = rr_constants.RISK_TYPES[2]
        elif total >= 75.00 and total < 100.00:
            risk_type = rr_constants.RISK_TYPES[3]
        elif total == 100.00:
            risk_type = rr_constants.RISK_TYPES[4]
        else:
            risk_type = None
        # retorno do risco total, da carteira de crédito, do total e do tipo de risco
        # (sendo esse último uma informação que pode ser gerada por uma tecnologia frontend)
        # até pensei em retirar, mas decidi manter
        return { "risk_total": risk_total,  "credit_wallet": credit_wallet, "total": total, "risk_type": risk_type }

    def category_code(self, response, category_code, operation_items):
        for i in range(0, len(response["operation_items"])):
            if response["operation_items"][i]["category_sub"]["category"]["category_code"] == category_code:
                operation_items.append(response["operation_items"][i])
        return operation_items

    def category_sub_code(self, response, operation_category_sub_code, category_sub_code):
        for i in range(0, len(response["operation_items"])):
            if response["operation_items"][i]["category_sub"]["category_sub_code"] == category_sub_code:
                operation_category_sub_code.append(response["operation_items"][i])
        return operation_category_sub_code

    def due_code(self, response, operation_due_code, due_code):
        for i in range(0, len(response["operation_items"])):
            if response["operation_items"][i]["due_type"]["due_code"] == due_code:
                operation_due_code.append(response["operation_items"][i])
        return operation_due_code


        