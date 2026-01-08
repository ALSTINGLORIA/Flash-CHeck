from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_invoice():
    items = []
    total = 0
    total_tax = 0


    for i in range(len(request.form.getlist('item_name'))):
        item_name = request.form.getlist('item_name')[i]
        quantity = int(request.form.getlist('quantity')[i])
        price = float(request.form.getlist('price')[i])
        tax_rate = float(request.form.getlist('tax')[i])  

        
        item_total = quantity * price
        item_tax = item_total * (tax_rate / 100) 

        
        total += item_total
        total_tax += item_tax

        
        items.append({
            'item_name': item_name,
            'quantity': quantity,
            'price': price,
            'tax_rate': tax_rate,
            'item_total': item_total,
            'item_tax': item_tax
        })

    final_amount = total + total_tax  

    return render_template('invoice.html', items=items, total=total, total_tax=total_tax, final_amount=final_amount)


if __name__ == '__main__':
    app.run(debug=True)
