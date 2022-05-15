import sqlite3


db = sqlite3.connect('store.db')
c=db.cursor()

def add_product(name,price,quantity,category):
    db.execute(
        f"INSERT INTO product (name,price,quantity,category) VALUES('%s','%s','%s','%s')" % (name,price,quantity,category))
    db.commit()
# to confirm email is not already registered
def search_employ(email):
    details = c.execute(f"SELECT * from employ WHERE email ='{email}'").fetchall()
    if details:
        return True
    else:
        return False
def add_employ(name,email,contact,password):
    db.execute(
            f"INSERT INTO employ (name,email,phone,password) VALUES('%s','%s','%s','%s')" % (name,email,contact,password))
    db.commit()
# for non dublicate category
def search_cate(name):
    details = c.execute(f"SELECT * from category WHERE name ='{name}'").fetchall()
    if details:
        return True
    else:
        return False
def add_category(name):
    db.execute(f"INSERT INTO category (name) VALUES('%s')" % (name))
    db.commit()
# only for product window category box
def cate_list():
    data = list()
    details = c.execute(f"SELECT name from category").fetchall()
    for x in range(len(details)):
        data.append(str(details[x][0]))
    return data

# to fill the main admin screen boxes
def box_list():
    emp = list()
    pro = list()
    cate = list()

    employ = c.execute(f"SELECT id,name from employ").fetchall()
    product = c.execute(f"SELECT id,name from product").fetchall()
    category = c.execute(f"SELECT * from category").fetchall()
    # making string list for employ
    for x in range(len(employ)):
        emp.append(str(employ[x][0]) + "-" + str(employ[x][1]))
    for x in range(len(product)):
        pro.append(str(product[x][0]) + "-" + str(product[x][1]))
    for x in range(len(category)):
        cate.append(str(category[x][0]) + "-" + str(category[x][1]))
    return emp, pro, cate
def searching_function(table,name):
    data=list()
    details = c.execute(f"SELECT id,name FROM '{table}' where name LIKE '%{name}%'").fetchall()
    for x in range(len(details)):
        data.append(str(details[x][0]) + "-" + str(details[x][1]))
    return data
# to diplay data
def get_alldata(table,val):
    data = list()
    details = c.execute(f"SELECT * FROM '{table}' where id ='{val}'").fetchall()
    for x in range(len(details[0])):
        data.append(details[0][x])
    return data

# epdate employ
def update_employ(id,name,email,phone,password):
        sql_update = "UPDATE employ SET name='%s', email='%s', phone='%s', password='%s' WHERE id='%s'" % (name,email,phone,password,id)
        x=c.execute(sql_update)
        db.commit()
        if x:
            return True
        else:
            False
def update_category(id,name):
    sql_update = "UPDATE category SET name='%s' WHERE id='%s'" % (name, id)
    x = c.execute(sql_update)
    db.commit()
    if x:
        return True
    else:
        False
def update_product(id,name,price,stock,category):
    sql_update = "UPDATE product SET name='%s', price='%s', quantity='%s', category='%s' WHERE id='%s'" % (
    name, price, stock, category, id)
    x = c.execute(sql_update)
    db.commit()
    if x:
        return True
    else:
        False

# delete data

def delete(table,id):
    c.execute(f"DELETE FROM '{table}' WHERE id='{id}'", )
    db.commit()

# //////////////////////////////////////
# //////////////user db////////////
def sort_cat(name):
    data = list()
    details = c.execute(f"SELECT id,name FROM product where category LIKE '%{name}%'").fetchall()
    for x in range(len(details)):
        data.append(str(details[x][0]) + "-" + str(details[x][1]))
    return data
# for login and signup admin
def search_admin_email(table,email):
    details = c.execute(f"SELECT * from '{table}' WHERE email ='{email}'").fetchall()
    if details:
        return True
    else:
        return False
def admin_signup(name,email,password):
    db.execute(
        f"INSERT INTO admin (name,email,password) VALUES('%s','%s','%s')" % (
        name, email, password))
    db.commit()
def verify_login(table,email,password):
    details = c.execute(f"SELECT * from '{table}' WHERE email ='{email}' And password='{password}'").fetchall()
    if details:
        return True
    else:
        return False
def user_signup(name,email,password,phone,address):
    db.execute(
        f"INSERT INTO user (name,email,password,phone,address) VALUES('%s','%s','%s','%s','%s')" % (
            name, email, password,phone,address))
    db.commit()

    # update product quantity after buying
def update_quantity(id, quantity):
    sql_update = "UPDATE product SET quantity='%s' WHERE id='%s'" % (quantity, id)
    x = c.execute(sql_update)
    db.commit()
def all_print():
    data=c.execute("SELECT * from product WHERE quantity<'20'").fetchall()
    return data
# update sold table
def sold_when_admin_add():
    data=c.execute("SELECT * FROM product").fetchall()
    last=len(data)-1
    c.execute(f"INSERT INTO sold (id,name,category,item_price,quantity,total) VALUES('%s','%s','%s','%s','%s','%s')" % (data[last][0],data[last][1],data[last][4],data[last][2],int(0),int(0)))
    db.commit()

# when product is updated it will be updated too sold
def sold_update_product_update(id,name,price,category):
    sql_update = "UPDATE sold SET name='%s', item_price='%s', category='%s' WHERE id='%s'" % (
        name, price, category, id)
    x = c.execute(sql_update)
    db.commit()
# when item is added to category it means it is sold
def sold_product(id,quantiy,total):
    t=c.execute("SELECT quantity, total from sold WHERE id='%s'"%id).fetchall()
    final_qt=int(t[0][0])+int(quantiy)
    final_pr=int(t[0][1])+int(total)
    sql_update = "UPDATE sold SET quantity='%s', total='%s' WHERE id='%s'" % (final_qt,final_pr, id)
    x = c.execute(sql_update)
    db.commit()
# taking all sold list
def all_sold():
    data=c.execute("SELECT * FROM sold").fetchall()
    return data
def cate_sold(category):
    data=c.execute("Select * from sold WHERE category='%s'" % (category)).fetchall()
    return data
def high_sold():
    data=c.execute("select * from sold order by quantity desc limit 0,3").fetchall()
    return data
def set_dis(pk1,dis1,pk2,dis2,pk3,dis3):
    sql_update = "UPDATE discount SET low='%s', medium='%s' WHERE id='1'" % (pk1,dis1)
    x = c.execute(sql_update)
    db.commit()
    sql_update = "UPDATE discount SET low='%s', medium='%s' WHERE id='2'" % (pk2,dis2)
    x = c.execute(sql_update)
    db.commit()
    sql_update = "UPDATE discount SET low='%s', medium='%s' WHERE id='3'" % (pk3,dis3)
    x = c.execute(sql_update)
    db.commit()
def get_dis():
    data=c.execute("SELECT * from discount").fetchall()
    return data
def order_now(name,t_price,quantity,status,discount,address):
    c.execute(f"INSERT INTO order_list (name,price,quantity,status,discount,address) VALUES('%s','%s','%s','%s','%s','%s')" % (name,t_price,quantity,status,discount,address))
    db.commit()
    id=c.execute("SELECT * from order_list").fetchall()
    last = len(id)-1
    return last
def get_discount_val():
    result=[]
    data=c.execute("SELECT * from discount").fetchall()
    for x in range(len(data)):
        result.append([int(data[x][1]),int(data[x][2])])
    return result
def get_order_id():
    id=c.execute("SELECT * from order_list").fetchall()
    return id
def mark_order(id):
    result=list()
    data=c.execute("SELECT id,name,price from order_list WHERE status='%s'" %id).fetchall()
    for x in range(len(data)):
        result.append(str(data[x][0])+"----"+str(data[x][1])+ "----"+str(data[x][2]))
    return result
def order_status(id,status):
    c.execute("UPDATE order_list SET status='%s' WHERE id='%s'" % (status,id))
    db.commit()
# for comment section only
def add_comment(keys,name,email,comment,reply):
    c.execute(f"INSERT INTO comments (keys,name,email,comment,reply) VALUES('%s','%s','%s','%s','%s')" % (keys,name,email,comment,reply))
    db.commit()
def get_all_comment(id):
    data=c.execute("SELECT id,name FROM comments WHERE keys='%s'" %id).fetchall()
    return data
def get_all_comment_no_specifi():
    data=c.execute("SELECT id,name FROM comments").fetchall()
    return data
def view_comment(id):
    data = c.execute("SELECT name,email,comment,reply FROM comments WHERE id='%s'" %id ).fetchall()
    return data
def update_comment(id,string):
    c.execute("UPDATE comments SET reply='%s' WHERE id='%s'" % (string, id))
    db.commit()
def product_details_geting():
    pro = list()
    product = c.execute(f"SELECT id,name from product").fetchall()
    # making string list for employ
    for x in range(len(product)):
        pro.append(str(product[x][0]) + "----" + str(product[x][1]))
    return  pro
def add_product_details(id,string):
        c.execute("UPDATE product SET details='%s' WHERE id='%s'" % (string, id))
        db.commit()
def sp_details(id):
    data=c.execute("SELECT details from product WHERE id='%s'" %id).fetchall()
    return data
def delete_comment(id):
    c.execute("DELETE FROM comments WHERE keys='%s'" %id)
    db.commit()

def low_saleing():
    data=c.execute("select * from sold order by quantity ASC limit 0,3").fetchall()
    return data