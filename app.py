from flask import Flask, render_template, make_response, jsonify, request, redirect, flash, session, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime
import requests


# # # # # # # # # # # #
# Config
#
app = Flask(__name__)
boostrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'e2e5c448583a7b8fb6f3e162ec0333a289e4c8e6eeeb95f2'   


# # # # # # # # # # # #
# Index
#
@app.route('/home')
@app.route('/')
def index():    
    api_endpoint = get_rest_address('/get_current')
    get_number_of_users = requests.get(api_endpoint)    
    return render_template('index.html', number_of_users=get_number_of_users.content.decode())


# # # # # # # # # # # #
# Routes
#
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':                
        
        # process form and store name in session
        this_form = request.form        
        name = this_form['name'] 
        session["user"] = name

        # make api call for new user login
        endpoint = '/new_login'
        api_endpoint = get_rest_address(endpoint)
        r = requests.post(api_endpoint, json={'name':name})                
        return redirect('/home')

    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():

    if "user" in session:
        user = session["user"]
    else:
        user = None
            
    if request.method == 'POST':                

        # process form and store name
        this_form = request.form        
        name = this_form['name']                
        
        # make api call for new user login
        endpoint = '/new_logout'
        api_endpoint = get_rest_address(endpoint)
        r = requests.post(api_endpoint, json={'name':name})
        
        print("r.status_code: ", r.status_code)
        print("type(r.status_code): ", type(r.status_code))

        if r.status_code == 200:        
            session.clear()
            return redirect('/home')        
        else:
            return render_template('logout.html', user=user)

    return render_template('logout.html', user=user)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/map')
def map():
    return render_template('map.html')    


# # # # # # # # # # # #
# Functions
#
def get_rest_address(endpoint):
    address = 'http://localhost:'
    port = '57775'                        
    return address + port + endpoint


# # # # # # # # # # # #
# Run
#
if __name__ == '__main__':
    app.run(port=47774, debug=True)

