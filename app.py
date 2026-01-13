from flask import request, redirect, render_template, Flask

app = Flask(__name__)

@app.route('/mypage/me')
def view_about_me():
    return render_template('/mypage/index_me.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def view_contact():
    if request.method == 'GET':
        return render_template('/mypage/index_contact.html')
    elif request.method == 'POST':
        print(request.form)
        return redirect('/')