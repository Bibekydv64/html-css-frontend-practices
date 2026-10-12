from flask import Flask,request,Response,redirect,session,url_for




app = Flask(__name__)
app.secret_key ='superkey'


@app.route('/',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('username')
        password = request.form.get('password')

        if user_name == 'admain' and password == 'password':
            session['user'] = user_name
            return redirect(url_for('Welcome!'))

        else:
            return Response('Invalid username and password!', mimetype=('text/plain'))

    return '''
            <h2>Login</h2>

        <form methods="POST">
            <div class="input-group">
                <label for="username">Username or Email</label>
                <input type="text" id="username" required autocomplete="off">
            </div>
            
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" required>
            </div>
            
            <button type="submit" class="login-btn" value='/' >Sign In</button>
            
        </form>
            '''

    return redirect(url_for('/'))






app.run(debug=True)