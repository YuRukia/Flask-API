from flask import Flask, jsonify, request, render_template, redirect, flash
import LoadFile, FindEntry, AddEntry, UpdateOrder

app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        result = FindEntry.find(LoadFile.load('./orders.json'), request.form['text'])
        if result != False:
            return result
        else:
            flash('Incorrect UUID')
            return render_template('uuid_query.html')
    return render_template('uuid_query.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        uuid = AddEntry.addOrder('','',0)
        flash('uuid: ' + uuid)
        return redirect('/add')
    return render_template('add_order.html', ButtonPressed = 0)

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    return jsonify(LoadFile.load('./orders.json'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        result = UpdateOrder.update(request.form)
        if result != False:
            flash('Order Updated')
        else:
            flash('Incorrect Input')
    return render_template('update_entry.html')

if __name__ == '__main__':
    app.run()
