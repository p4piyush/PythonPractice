from config import app,db
from flask import request
from model import Product
#uri --> http://localhost:5000/api/v1/product/  -- GET

import json
@app.route('/api/v1/product/',methods=['GET'])
def get_list_of_products():
    #fetch list of products from db -- thru sqlalchemy
    product_list = Product.query.all()

    #if no products in db -- return -- simple message --
    if not product_list:
        return json.dumps({"ERROR" : "No Products...!"})

    final_product_list = []
    #iterate one by and prepare dict -
    for prod in product_list:
        prod_dict = {}
        prod_dict['PRODUCT_ID'] = prod.id
        prod_dict['PRODUCT_NAME'] = prod.name
        prod_dict['PRODUCT_PRICE'] = prod.price
        prod_dict['PRODUCT_QTY'] = prod.qty
        prod_dict['PRODUCT_VENDOR'] = prod.vendor
        prod_dict['PRODUCT_CATEGORY'] = prod.category

        #add that dict every time inside final list
        final_product_list.append(prod_dict)

    if final_product_list:
        return json.dumps(final_product_list)





#http://localhost:5000/api/v1/product/  -- POST

@app.route('/api/v1/product/',methods=['POST'])
def save_product():
    #print(request.__dict__)
    #print(dir(request))
    #print(request.get_json())
    req_data = request.get_json()       # req_data -- is the dict

    #if not req_data:
    #    return json.dumps({"ERROR" : "Invalid Params to create a Product"})

    MANDATORY_FIELD = ["PRODUCT_NAME", "PRODUCT_QTY", "PRODUCT_PRICE", "PRODUCT_CATEGORY", "PRODUCT_VENDOR"]
    keys = req_data.keys()
    print(keys)
    for mfield in MANDATORY_FIELD:
        if mfield not in keys:
            return json.dumps({"ERROR": f"{mfield} field is missing"})

    if str(req_data.get('PRODUCT_PRICE')).isalpha() or req_data.get('PRODUCT_PRICE')<=0:
        return json.dumps({"ERROR" : "Invalid Product Price"})

    try:
        prod = Product(name=req_data.get('PRODUCT_NAME'),
                qty=req_data.get('PRODUCT_QTY'),
                price=req_data.get('PRODUCT_PRICE'),
                category=req_data.get('PRODUCT_CATEGORY'),
                vendor=req_data.get('PRODUCT_VENDOR'))
        db.session.add(prod)
        db.session.commit()
    except:
        return json.dumps({"ERROR" : "Problem in Adding a Product"})
    else:
        return json.dumps({"SUCCESS": "Product Added Successfully..."})


#http://localhost:5000/api/v1/product/{id}  --> put -- {requestbody}

@app.route('/api/v1/product/<int:pid>',methods=['PUT'])
def update_product_information(pid):

    db_product = Product.query.filter_by(id=pid).first()
    if db_product:
        req_data = request.get_json()

        MANDATORY_FIELD = ["PRODUCT_NAME", "PRODUCT_QTY", "PRODUCT_PRICE", "PRODUCT_CATEGORY", "PRODUCT_VENDOR"]
        keys = req_data.keys()
        print(keys)
        for mfield in MANDATORY_FIELD:
            if mfield not in keys:
                return json.dumps({"ERROR": f"{mfield} field is missing"})

        db_product.name = req_data.get('PRODUCT_NAME')
        db_product.qty = req_data.get('PRODUCT_QTY')
        db_product.price = req_data.get('PRODUCT_PRICE')
        db_product.vendor = req_data.get('PRODUCT_VENDOR')
        db_product.category = req_data.get('PRODUCT_CATEGORY')
        db.session.commit()
        return json.dumps({"SUCCESS": "Product UPdated.. Successfully..."})
    else:
        return json.dumps({"ERROR": "Product With Given Id Cannot Be Updated/Found.."})


@app.route('/api/v1/product/<int:pid>',methods=['DELETE'])
def delete_product(pid):
    db_product = Product.query.filter_by(id=pid).first()
    if db_product:
        db.session.delete(db_product)
        db.session.commit()
        return json.dumps({"SUCCESS": "Product Removed Successfully..."})
    else:
        return json.dumps({"ERROR": "Product With Given Id Cannot Be Deleted/Found.."})