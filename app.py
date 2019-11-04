from flask import *
import mlab
from models.clothers import Clothers
from models.mancloth import Mancloth
from models.orderproduct import Orderproduct
from models.customer_infor import Customerinfor
app = Flask(__name__)

mlab.connect()


@app.route('/')
def index():
    allproduct = Orderproduct.objects()
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
    return render_template("index.html",indexnum=indexnum)

@app.route('/woman')
def woman():
    allproduct = Orderproduct.objects()
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
    # get all document from dabase
    all_clother = Clothers.objects()
    return render_template("woman.html",all_clother= all_clother,indexnum=indexnum)

@app.route('/womandetail/<womanid>', methods = ["GET","POST"])
def womandetail(womanid):
    allproduct = Orderproduct.objects()
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
    woman_id = Clothers.objects.with_id(womanid)
    if request.method == "GET":
        return render_template("womandetail.html",woman_id  = woman_id,indexnum=indexnum )
    else:
        form = request.form
        orderproduct = Orderproduct(
            title = woman_id["title"],
            price = woman_id["price"],
            image = woman_id["image"],
            size = form["size"],
            count = form["count"]
        )
        orderproduct.save() 
        return redirect(url_for('shoppcard'))

@app.route('/man')
def man():
    allproduct = Orderproduct.objects()
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
    all_clothman = Mancloth.objects()
    return render_template("man.html",all_clothman = all_clothman,indexnum=indexnum)

@app.route('/detail/<imgid>', methods = ["GET","POST"])
def detail(imgid):
    allproduct = Orderproduct.objects()
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
    img_id = Mancloth.objects.with_id(imgid)
    if request.method == "GET":
        return render_template("detail.html",img_id = img_id,indexnum=indexnum)
    else:
        form = request.form
        orderproduct = Orderproduct(
            title = img_id["title"],
            price = img_id["price"],
            image = img_id["image"],
            size = form["size"],
            count = form["count"]
        )
        orderproduct.save()        
        return redirect(url_for('shoppcard'))  
  

@app.route('/shoppcard')
def shoppcard():
    allproduct = Orderproduct.objects()
    total = 0 
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
        total += product.price * product.count         
    return render_template("shoppcard.html", allproduct = allproduct,total = total,indexnum = indexnum)

@app.route('/delete/<productid>')
def delete(productid):
    product_to_delete = Orderproduct.objects.with_id(productid)
    if product_to_delete is not None:
        product_to_delete.delete()
        return redirect(url_for('shoppcard'))
    else:
        return "Service not found"


@app.route('/payment', methods = ["GET","POST"])
def payment():
    allproduct = Orderproduct.objects()
    indexnum = 0 
    total = 0
    listordered = []
    for product in allproduct:
        indexnum += 1
        total += product.price * product.count
        title = product["title"]
        price = product["price"]
        size = product["size"]
        count = product["count"]
        listordered.append(title)
        listordered.append(price)
        listordered.append(count)
        listordered.append(size)
    if request.method == "GET":
        return render_template('payment.html',indexnum = indexnum,allproduct = allproduct,total = total)
    else:
        form = request.form
        customerinfor = Customerinfor(           
            listordered = listordered,
            total = total,
            name = form["name"],
            numberphone = form["numberphone"],
            mail = form["mail"],
            city = form["city"],
            district = form["district"],
            address = form["address"],
           
        )
        customerinfor.save()
        
        return redirect(url_for('success'))
    
 
@app.route('/success')
def success():
    # delete product from the shopping card when order success
    all_orderproduct = Orderproduct.objects()
    all_orderproduct.delete()
    return render_template("success.html")



if __name__ == '__main__':
    app.run(debug=True)