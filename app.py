import falcon
from api.resources.home import Home
from api.resources.limit import Limit
from api.resources.financing import Financing
from api.resources.leasing_operations import LeasingOperations
from api.resources.lending import Lending
from api.resources.discounted_securities import DiscountedSecurities
from api.resources.co_obligations import CoObrigations
from api.resources.advances_depositors import AdvancesDepositors


def create():
    api = falcon.API()
    api.add_route('/', Home())

    api.add_route('/advances-depositors', AdvancesDepositors())
    api.add_route('/advances-depositors/category-sub-code/{category_sub_code:int}', AdvancesDepositors())
    api.add_route('/advances-depositors/due-code/{due_code:int}', AdvancesDepositors())

    api.add_route('/co-obligations', CoObrigations())
    api.add_route('/co-obligations/category-sub-code/{category_sub_code:int}', CoObrigations())
    api.add_route('/co-obligations/due-code/{due_code:int}', CoObrigations())

    api.add_route('/discounted-securities', DiscountedSecurities())
    api.add_route('/discounted-securities/category-sub-code/{category_sub_code:int}', DiscountedSecurities())
    api.add_route('/discounted-securities/due-code/{due_code:int}', DiscountedSecurities())

    api.add_route('/financing', Financing())
    api.add_route('/financing/category-sub-code/{category_sub_code:int}', Financing())
    api.add_route('/financing/due-code/{due_code:int}', Financing())

    api.add_route('/leasing-operations', LeasingOperations())
    api.add_route('/leasing-operations/category-sub-code/{category_sub_code:int}', LeasingOperations())
    api.add_route('/leasing-operations/due-code/{due_code:int}', LeasingOperations())

    api.add_route('/lending', Lending())
    api.add_route('/lending/category-sub-code/{category_sub_code:int}', Lending())
    api.add_route('/lending/due-code/{due_code:int}', Lending())
    
    api.add_route('/limit', Limit())
    api.add_route('/limit/category-sub-code/{category_sub_code:int}', Limit())
    api.add_route('/limit/due-code/{due_code:int}', Limit())

    return api

app = application = create()
