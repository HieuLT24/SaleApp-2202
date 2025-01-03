from flask import render_template, request, redirect
import dao
from app import app, login
import  math
from flask_login import login_user, logout_user

@app.route("/")
def index():

    cates = dao.load_categories()
    cate_id = request.args.get('category_id')

    page = request.args.get('page', 1)
    page_size = app.config["PAGE_SIZE"]
    total = dao.count_products()

    kw = request.args.get('kw')
    prods = dao.load_products(cate_id=cate_id, kw=kw, page=int(page))

    return render_template("index.html", categories=cates, products=prods,
                           pages = math.ceil(total/page_size))


@app.route('/register', methods=['get', 'post'])
def register_view():
    err_msg =''
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if not password.__eq__(confirm):
            err_msg='MAT KHAU KHONG TRUNG KHOP!'

        else:
            data = request.form.copy()
            del data["confirm"]
            avatar = request.files.get('avatar')
            dao.add_user(avatar = avatar, **data)

            return redirect('/login')
    return render_template('register.html', err_msg=err_msg)

@app.route('/login', methods=['get', 'post'])
def login_view():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user = user)
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout_process():
    logout_user()
    return redirect('/login')

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    app.run(debug=True)
