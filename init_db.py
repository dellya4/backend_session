from ..wishMe import create_app, db

app = create_app()

with app.app_contect():
    db.create_all()
    print("База данных успешно создана!")