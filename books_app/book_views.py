print("books_view.py")
from books_app import app
from books_app import book_controller
from flask import jsonify,request

@app.route('/',methods=['GET'])
def home():
    return jsonify(msg="Home Page"), 200


@app.route('/insert_data', methods=['POST'])
def insert_data_view():
    data = request.get_json(silent=True)
    if data:
        res = book_controller.insert_data_controller(data)
        return jsonify(msg=res), 201
    return jsonify(msg="provide all details"), 403

@app.route('/get_all', methods=['GET'])
def get_all_view():
    res = book_controller.get_all_controller()
    return jsonify(msg=res), 200

@app.route('/fetch_one/<column_name>/<value>', methods=['GET'])
def get_one_view(column_name,value):
    res=book_controller.get_one_controller(column_name,value)
    if res["status"] == "success":
        return jsonify(res), 200  
    else:
        return jsonify(res), 404
    
@app.route("/delete_one/<column_name>/<value>", methods=['DELETE'])
def delete_one_view(column_name,value):
    book_controller.delete_one_controller(column_name,value)
    return jsonify(msg='deleted'),200

@app.route('/update_one',methods=['PATCH'])
def update_one_view():
    res=book_controller.update_one_controller()
    return jsonify(msg=res),200

@app.route('/update_all',methods=['PATCH'])
def update_all_view():
    res=book_controller.update_all_controller()

    return jsonify(msg=res),200

@app.route('/update_record/<int:record_id>', methods=['PATCH'])
def update_record_view(record_id):
    update_data = request.json
    if not update_data:
        return jsonify({"status": "failure", "message": "No update data provided."}), 400
    result = book_controller.update_all_columns_controller(update_data, record_id)

    if result["status"] == "success":
        return jsonify(result), 200  
    else:
        return jsonify(result), 400


    