from learn_restful_db import Customer,jsonify, app, db
from flask_sqlalchemy import SQLAlchemy


@app.route('/getCustomers' , methods= ['GET'])
def getCustomers():
    results = []
    for customer in Customer.query.all():
        results.append({'id': customer.id,'name' : customer.name,'location': customer.location})
    return jsonify({'customers':results})


@app.route('/getCustomers/<int:cust_id>', methods=['GET'])
def get_by_cust_id(cust_id):
    result = Customer.query.get(cust_id)
    detail = []
    detail.append({'id':result.id,'name':result.name,'location':result.location})
    return jsonify({'customer':detail})


if __name__ == '__main__':
    app.run(debug=True)