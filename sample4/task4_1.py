from flask import Flask, request
from flask import render_template
from sample4.db_manager import DbCommands

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def show_person():
    return render_template('main.html', category=DbCommands.get_category())


@app.route('/<name>')
def show_category(name):
    if name in DbCommands.get_category():
        return render_template('category.html', title=name, products=DbCommands.get_product_info())
    else:
        return "404page"


@app.route('/<category>/<name>')
def show_product(category, name):
    if name in DbCommands.get_product():
        return render_template('items.html', title=name, products=DbCommands.get_product_info())
    else:
        return "404page"


@app.route('/admin', methods=["GET", "POST"])
def admin():
    dictionary = dict(request.form)
    if dictionary.get('cat') is not None:
        name = dictionary.get("category")
        if name is None:
            pass
        else:
            DbCommands.send_new_category(name)

    else:
        product = dictionary.get('product')
        category_add = dictionary.get('category_add')
        valuable = dictionary.get('valuable')
        price = dictionary.get('price')
        quantity = dictionary.get('quantity')

        if product is None:
            pass
        else:
            DbCommands.send_new_item(product, valuable, price, quantity, category_add)

    return render_template('admin.html', category=DbCommands.get_category())


if __name__ == '__main__':
    app.run(debug=True)
