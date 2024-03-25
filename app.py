# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, redirect,url_for, request, flash
from datetime import timedelta
# import mysql.connector
# from markupsafe import escape
# db=mysql.connector.connect()
# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="ell887"
# )

# mycursor=db.cursor()

# # mycursor.execute("CREATE TABLE item_list (item_name VARCHAR(50), item_id smallint PRIMARY KEY)")
# mycursor.execute("CREATE TABLE IF NOT EXISTS item_list_4 (id INT PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL) ")

app =Flask(__name__)
# app.secret_key="hello"
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# app.permmanent_session_lifetime=timedelta(minutes=5)
# db=SQLAlchemy(app)



# with app.app_context():
#     db.create_all()


# class users(db.Model):
#     _id=db.Column("id",db.Integer, primary_key=True)
#     name=db.Column(db.String(100))
#     item_id=db.Column(db.Integer)

#     def __init__(self,name,item_id):
#         self.name=name
#         self.item_id=item_id

# def db_display(item_id):
#     mycursor.execute(f"SELECT * from item_list_4 WHERE item_id={item_id}")

# def db_delete(item_id_to_delete):
#     item_id_to_delete=int(item_id_to_delete)
    
#     try:
#         mycursor.execute(f"DELETE FROM item_list_4 WHERE item_id={item_id_to_delete}")
#         db.commit()
#         print(f"deleted id '{item_id_to_delete}'")
#     except Exception as e:
#         print(e)

# def db_insert(item_name,item_id):
#     try:
#             mycursor.execute("INSERT INTO item_list_4 (item_id, item_name) VALUES (%s, %s)", (item_id, item_name))
#             print(f"Inserted item '{item_name}' with id '{item_id}'")
#             db.commit()

 
#         # db.commit()
#     except Exception as e:
#         # print(f"error in inserting item '{item_name}' with id '{item_id}'")
#         # print("error")
#         print(f"{e}")
#         pass



global index_counter
index_counter=10
job_dict={}
for x in range(index_counter):
    job_dict[int(x+1)]=f"Item {(x+1)}"
    # db_insert(job_dict[int(x+1)],int(x+1))

    # usr=users(job_dict[int(x+1)],int(x+1))
    # db.session.add(usr)
    # db.session.commit() 





# print(JOBS)
# mycursor.execute("SELECT * from item_list_4 ORDER BY id ASC")


# mycursor.execute("ALTER TABLE item_list_4 CHANGE name item_name varchar(50)")
# mycursor.execute("ALTER TABLE item_list_4 CHANGE id item_id int")


#     db_display(x)


def is_convertible_to_int(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False



# JOBS=[
#     {'id':1,
#     'title':"Item 1",
#     'price': 'RS 150'
#     }

# ]
# mycursor.close()
# db.close()
@app.route("/",methods=['GET', 'POST'])

def home():
    
    # index_counter
    
    # print(index_counter)
    if request.method == 'POST':
        if 'add_item' in request.form:
            item = request.form['item']
            item_id=request.form['item_id']
            print(f"item to add is {item}, item_id is {item_id}")

            
            if is_convertible_to_int(item_id):
                if (int(item_id) not in job_dict):
            # index_counter =index_counter+ 1
                    print(f"item id is {item_id}")
                    job_dict[int(item_id)] = item
                    # db_insert(job_dict[int(item_id)],int(item_id))
                    # found_user=users.query.filter_by(item_id).first()
                    # if found_user:
                    #     pass
                    # else:
                    #     usr=users(item,item_id)
                    #     db.session.add(usr)
                    #     db.session.commit()

                else:
                    print("invalid entry: already in list")
                    # flash("invalid entry: already in list","info")
            else:
                print("invalid entry: unique id has to be integer")
                # flash("invalid entry: unique id has to be integer","info")
            # items.append(item)
        elif 'remove_item' in request.form:
            
            index_to_remove=request.form['remove_item_id']
            print(f'index to remove {index_to_remove}')
            if is_convertible_to_int(index_to_remove):
                index_to_remove=int(index_to_remove)
                if index_to_remove in job_dict:
                    print(f"index is {job_dict[index_to_remove]}")
                    del job_dict[index_to_remove]
                    # db_delete(int(index_to_remove))
                else:
                    print("Index not found")
                    # flash("Index not found")
            else:
                print("invalid entry: unique id has to be integer","info")
                # flash("invalid entry: unique id has to be integer","info")

    

    return render_template("base.html",job_dict=job_dict)

@app.route("/test")

def testy():
    return render_template("index.html")


@app.route("/api/jobs")
 
# def list_jobs():
#     mycursor.execute("SELECT * from item_list_4 ORDER BY item_id ASC")
#     result_dict = dict(mycursor)
#     return jsonify(result_dict)
#     # return render_template("view.html",values=users.query.all())


# @app.route('/')
# def home():
#     return "hello world this is the main page <h1> hello </h1>"
@app.route("/<name>")
def user(name):
    return f"hello {name}"
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__=='__main__':
    # db.create_all()
    app.run(host='0.0.0.0',debug=True)

