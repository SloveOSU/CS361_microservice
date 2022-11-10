from flask import Flask, render_template, make_response, jsonify, request, redirect
from flask_bootstrap import Bootstrap
from datetime import datetime

# # # # # # # # # # # #
#
app = Flask(__name__)
boostrap = Bootstrap(app)


# # # # # # # # # # # #
# Errorhandlers
# 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# # # # # # # # # # # #
# Index
#
@app.route('/')
def index():        
    return render_template('index.html')


# # # # # # # # # # # #
# Routes
#
@app.route('/user/<name>')
def user(name):        
    return render_template('user.html', name=name)


@app.route('/test_string', methods=['GET'])
def test_string():        
    return '<h1>Test Successful!</h1>'


@app.route('/test_json', methods=['GET'])
def test_json():        
    return {'test' : 'success'}


# # # # # # # # # # # #
# API Routes: Logins
#
current_users = []
@app.route('/login', methods=['POST'])
def login():    

    if request.method == 'POST':

        print('before current_users: ', current_users)

        # field post request    
        req_data = request.get_json()
        name = req_data['name']

        # check to see if value is in dictionary
        if name not in current_users:
            current_users.append(name)
        else:
            return '<h1>You are already logged in as {}.</h1>'.format(name)
        
    print('after current_users: ', current_users)                
    return '<h1>Welcome, {}!</h1>'.format(name)


@app.route('/logout', methods=['POST'])
def logout():
    print('before current_users: ', current_users)
    req_data = request.get_json()
    name = req_data['name']

    if name in current_users:
        current_users.remove(name)
    else:        
        return '<h1>Please login to your account</h1>'

    print('after current_users: ', current_users)
    return '<h1>You have signed out of your account</h1>'


@app.route('/current', methods=['GET'])
def current():
    return jsonify(current_users)















# # # # # # # # # # # #
# Checkout Microservice
#

# # # # # # # # # # # #
#   /checkout
# # # # # # # # # # # #
#   This endpoint accepts a POST request containing a numeric value representing checkout length
#   A date object is then formated to represent today in a number within 1 and 366.
#   Calculations are then performed to determine the return date and days until return is due
#
@app.route('/checkout', methods=['POST'])
def checkout():    
    req = request.get_json()                                                        # decode JSON request object 
    allowed_days_checkout = req['allowed_days_checkout']                            # store POST data
    today_in_days = datetime.now().strftime("%j")                                   # needs a db for full function
    checkout_date_in_days = datetime.now().strftime("%j")                           # format datetime object to day kind
    return_date_in_days = int(checkout_date_in_days) + int(allowed_days_checkout)   # determine return date 
    days_left_until_return_due = int(return_date_in_days) - int(today_in_days)      # determine days until return is due    
    return jsonify({                                                                # return data as JSON object
        "date_due": return_date_in_days,                                                
        "days_left_until_return" : days_left_until_return_due                           
        }) 






# # # # # # # # # # # #
# App.run()
#
if __name__ == '__main__':    
    app.run(port=47774, debug=True, use_reloader=True)









# # # # # # # # # # # #
# Test Requests/Response
#

# # # # # # # # # # # #
# /checkout POST
''' 
Request: 
    curl -X POST 127.0.0.1:47774/checkout -H 'Content-Type: application/json' -d '{"allowed_days_checkout":"5"}'
Response:
    {
    "date_due": 319, 
    "days_left_until_return": 5
    }
'''