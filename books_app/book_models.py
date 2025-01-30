from sqlalchemy import text
from books_app import db

def create_table():
    query=text(""" CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),description VARCHAR(50),author VARCHAR(50))""")
    db.session.execute(query)
    db.session.commit()
    return " Table Created Successfully"

def create_table():
     query=text(""" CREATE TABLE IF NOT EXISTS book_price(book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                id INTEGER NOT NULL,price DECIMAL NOT NULL,FOREIGN KEY (id) REFERENCES books (book_id))
""")
     db.session.execute(query)
     db.session.commit()
     return " book_price Created Successfully"

def insert_data_model(data):
    query=text(""" INSERT INTO books(name,description,author) VALUES
               (:name, :description, :author)
""")
    values = {"name": data['name'], "description": data['description'], "author": data['author']}
    db.session.execute(query, values)
    db.session.commit()
    return "data inserted successfully"

def get_all_model():
    query = text("""SELECT * FROM books""")
    res = db.session.execute(query)
    data =res.fetchall()
    print("data ========", data)
    return data
def get_one(column_name,value):
     query=text(f" SELECT * FROM books WHERE {column_name} = :value LIMIT 1")
     res=db.session.execute(query,{"value":value})
     record = res.mappings().first()
     return dict(record) if record else None

def delete_one(column_name,value):
     query=text(f"DELETE FROM books WHERE{column_name}=:value LIMIT 1 ")
     db.session.execute(query,{"value":value})
     db.session.commit()
     return "deleted"
     
       

def update_one():
    query=text(""" UPDATE BOOKS SET author='Reedhema'
               WHERE ID=2 """)
    db.session.execute(query)
    db.session.commit() 
    print("Data updated successfully")
    return True  
def Update_all():
    query=text(""" UPDATE BOOKS SET name=:name,description=:description,author=:author WHERE id=2
""")
    params={"name":"Book2","description":" This is book two","author":" Reedhema"}
    db.session.execute(query,params)
    db.session.commit()
    return {"status":"success","msg":"All valuees update sucessfully"}

def update_all_columns_dynamic(update_data, record_id):
    
        set_clause = ", ".join(f"{key} = :{key}" for key in update_data.keys())
        query = text(f"UPDATE BOOKS SET {set_clause} WHERE ID = :id")
        update_data["id"] = record_id  
        db.session.execute(query, update_data)
        db.session.commit()
        return {"status": "success", "message": "All values updated successfully."}
    
        
    