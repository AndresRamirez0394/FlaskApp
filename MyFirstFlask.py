from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username[0].isupper() and any(char.isdigit() for char in password):
            return 'Login successful'
        else:
            return render_template('login.html')
    
    else:
        return render_template('login.html')
    
@app.route('/success/<username>')
def success(username):
    return f'<h1>Login Successful! {username}!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
