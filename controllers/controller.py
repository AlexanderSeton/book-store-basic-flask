from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title = "All Orders", orders = orders)

# @app.route('/orders/<index>')
# def get_one_order(index):
#     list = []
#     list.append(orders[int(index)])
#     return render_template('index.html', title = "Individual Order", orders = list)

@app.route('/orders/<index>')
def get_one_order(index):
    individual_order = orders[int(index)]
    completed_html = render_template('order.html', title = "Individual Order", order = individual_order)
    return completed_html

