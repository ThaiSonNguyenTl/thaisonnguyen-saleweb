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
# delete product in shopcard
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
    count = 0
    listordered = []
    for product in allproduct:
        indexnum += 1
        total += product.price * product.count
        count += product.count
        title = product["title"]
        image = product["image"]
        everyProCount = product["count"]
        listordered.append(title)
        listordered.append(image)
        listordered.append(everyProCount)
    if request.method == "GET":
        return render_template('payment.html',indexnum = indexnum,allproduct = allproduct,total = total)
    else:
        form = request.form
        customerinfor = Customerinfor(           
            listordered = listordered,
            total = total,
            count = count,
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
    indexnum = 0 
    for i in all_orderproduct:
        indexnum += 1
    return render_template("success.html",indexnum = indexnum)
# admin customer order product
@app.route('/admin')
def admin():
    all_infor = Customerinfor.objects()
    return render_template("admin.html",all_infor = all_infor)
# delete infor customer order
@app.route('/admindelete/<inforid>')
def admindelete(inforid):
    admin_delete = Customerinfor.objects.with_id(inforid)
    if admin_delete is not None:
        admin_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"
# admin all product man,woman
@app.route('/adminProduct')
def adminProduct():
    allproduct = Mancloth.objects()
    all_clother = Clothers.objects()
    x = len(allproduct)
    return render_template("adminProduct.html",allproduct = allproduct,all_clother = all_clother,x=x)
# delete product man
@app.route('/deleteProduct/<productid>')
def deleteProduct(productid):
    product_delete = Mancloth.objects.with_id(productid)
    if product_delete is not None:
        product_delete.delete()
        return redirect(url_for('adminProduct'))
    else:
        return "Service not found"
# repair product man

# delete product woman
@app.route('/deleteWoman/<prodwomanid>')
def deleteWoman(prodwomanid):
    delete_product_woman = Clothers.objects.with_id(prodwomanid)
    if delete_product_woman is not None:
        delete_product_woman.delete()
        return redirect(url_for('adminProduct'))
    else:
        return "Service not found"

@app.route('/createWoman', methods = ["GET","POST"])
def createWoman():
    if request.method == "GET":
        return render_template("createWoman.html")
    else:
        form = request.form
        createwoman = Clothers(
            title = form["title"],
            image = form["image"],
            price = form["price"]
        )
        createwoman.save()
        return redirect(url_for('adminProduct'))

@app.route('/createMan', methods = ["GET","POST"])
def createMan():
    if request.method == "GET":
        return render_template("createMan.html")
    else:
        form = request.form
        createman = Mancloth(
            title = form["title"],
            image = form["image"],
            price = form["price"]
        )
        createman.save()
        return redirect(url_for('adminProduct'))

@app.route('/adminAll')
def adminAll():
    return render_template("adminAll.html")

if __name__ == '__main__':
    app.run(debug=True)