from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1. Veritabanı Ayarı: Proje klasöründe 'todo.db' adında bir dosya oluşturur
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

# 2. Veritabanı Modeli (Class yapısını burada kullanıyoruz)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=False)

# 3. Ana Sayfa: Görevleri Listele
@app.get("/")
def index():
    todo_list = Todo.query.all() # Veritabanındaki tüm görevleri çek
    return render_template("index.html", todo_list=todo_list)

# 4. Görev Ekleme
@app.post("/add")
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit() # Veritabanına kaydet
    return redirect(url_for("index"))

# 5. Görev Silme
@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Uygulama başlarken veritabanı tablosunu oluştur
    app.run(debug=True)