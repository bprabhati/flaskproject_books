print("run.py")
from books_app import app
from books_app.book_models import create_table


if __name__ == '__main__':
    with app.app_context():
        create_table()
    app.run() 