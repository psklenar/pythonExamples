from flask import Flask, jsonify, request, session
from flask_httpauth import HTTPBasicAuth


my_account = Flask(__name__)
#my_account.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
userlist = [
    {'jdoe': 'secretpassword'}
]

incomes = [
    {'description': 'salary', 'amount': 5000}
]

outcomes = [
    {'description': 'money_what_you_spend', 'amount': 0}
]

total = {'amount': 10}


auth = HTTPBasicAuth()


@my_account.route('/rest-auth')
@auth.login_required
def get_response():
    return jsonify('You are an authenticate person to see this message')


@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'roy' and password == 'roy':
            return True
        else:
            return False
    return False


@my_account.route('/incomes/<description>')
@auth.login_required
def get_incomes_from_description(description):
    returncode = 400
    tmp = []
    for polozka in incomes:
        if description in polozka['description']:
            tmp.append(polozka)
            returncode = 200

    return jsonify(tmp), returncode


@my_account.route('/incomes', methods=['POST'])
@auth.login_required
def add_income():
    incomes.append(request.get_json())
    return '', 204


@my_account.route('/outcomes')
@auth.login_required
def get_outcomes():
    return jsonify(outcomes)


@my_account.route('/outcomes', methods=['POST'])
@auth.login_required
def add_outcome():
    outcomes.append(request.get_json())
    return '', 204


@my_account.route('/zustatek')
@auth.login_required
def get_zustatek():
    sumarize = 0
    for i in incomes:
        sumarize += (i['amount'])

    for i in outcomes:
        sumarize -= (i['amount'])
    print(sumarize)
    total['amount'] = sumarize
    return jsonify(total)
