from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    # Collect input data from form
    product_cost = float(request.form['product_cost'])
    marketing_cost_per_product = float(request.form['marketing_cost_per_product'])  # Per product
    sales_price = float(request.form['sales_price'])
    quantity_sold = int(request.form['quantity_sold'])
    return_rate = float(request.form['return_rate']) / 100
    return_cost = float(request.form['return_cost'])
    overhead_costs = float(request.form['overhead_costs'])
    shipping_cost_per_product = float(request.form['shipping_cost_per_product'])

    # Perform calculations
    total_revenue = sales_price * quantity_sold
    total_product_cost = product_cost * quantity_sold
    total_costs = total_product_cost + overhead_costs
    cost_of_returns = return_rate * return_cost * quantity_sold
    total_marketing_cost = marketing_cost_per_product * quantity_sold
    total_shipping_cost = shipping_cost_per_product * quantity_sold
    net_profit = total_revenue - (total_costs + cost_of_returns + total_marketing_cost + total_shipping_cost)

    # Break-even Marketing Cost per Sale Calculation
    overhead_per_unit = overhead_costs / quantity_sold
    return_cost_per_unit = return_rate * return_cost
    break_even_marketing_cost_per_product = sales_price - (
                product_cost + return_cost_per_unit + overhead_per_unit + shipping_cost_per_product)

    # Pass results to the result template
    return render_template('result.html',
                           total_revenue=total_revenue,
                           total_costs=total_costs,
                           cost_of_returns=cost_of_returns,
                           total_marketing_cost=total_marketing_cost,
                           total_shipping_cost=total_shipping_cost,
                           net_profit=net_profit,
                           break_even_marketing_cost_per_product=break_even_marketing_cost_per_product)


if __name__ == '__main__':
    app.run(debug=True)
