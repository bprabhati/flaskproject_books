print("book_controller.py")
from books_app import book_models

def insert_data_controller(data):
    res=book_models.insert_data_model(data)
    return res

def get_all_controller():
    res=book_models.get_all_model()
    data_from_db = [{"id": each[0], 'name':each[1], 'description': each[2], 'author': each[3]} for each in res]
    return data_from_db

def get_one_controller(column_name,value):
    res=book_models.get_one(column_name,value)
    if res:
        return {"status": "success", "data": res}
    else:
        return {"status": "failure", "message": "Record not found."}
def delete_one_controller(column_name,value):
    res=book_models.delete_one(column_name,value)
    if res:
        return {"status": "successfully deleted"}
    else:
        return {"status": "failure", "message": "Record not found."}


def update_one_controller():
   success= book_models.update_one()
   if success:
        return {"status": "success", "message": "Book updated successfully."}
   else:
        return {"status": "failure", "message": "Failed to update the book."}
    
def update_all_controller():
   success= book_models.Update_all()
   if success:
        return {"status": "success", "message": "Book updated successfully."}
   else:
        return {"status": "failure", "message": "Failed to update the book."}
   
def update_all_columns_controller(update_data, record_id):
    result = book_models.update_all_columns_dynamic(update_data, record_id)
    return result
    