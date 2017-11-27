from flask import Blueprint, request, jsonify, abort
from .models import Loan
from .utils import JSONEncoder

import traceback

loan_blueprint = Blueprint('loan', __name__)


@loan_blueprint.route('/', methods=['GET', 'POST'])
def root():
    try:
        m = None
        if request.method == 'POST':
            if request.form.get('userNo') is None:
                m = Loan(cellPhone=request.values['cellPhone'], password=request.values['password'])
                m.save()
            else:
                m = Loan(userNo=int(request.values['userNo']))
                m.save()
            return jsonify({'loanId': m['loanId']})
        elif request.method == 'GET':
            userno = int(request.values['userNo'])
            m = Loan.query.raw_output().filter(Loan.userNo == userno).first()
    except Exception as e:
        print(e)
        abort(500)
    return JSONEncoder().encode(m)


@loan_blueprint.route('/addInfo', methods=['POST'])
def add():
    m = None
    try:
        exloan = Loan.query.filter(Loan.loanId == request.values['loanId']).first()
        exloan.fromdict(request.values).save()
        m = Loan.query.raw_output().filter(Loan.loanId == request.values['loanId']).first()
    except Exception as e:
        traceback.print_exc()
        abort(500)
    return JSONEncoder().encode(m)


@loan_blueprint.route('/none_apply', methods=['GET'])
def none_apply():
    if request.form.get('userNo') is None:
        m = Loan.query.raw_output().filter(
            Loan.cellPhone == request.values['cellPhone'] and Loan.password == request.values['password']
        ).first()
    else:
        m = Loan.query.raw_output().filter(Loan.userNo == int(request.values['userNo'])).first()
    return JSONEncoder().encode(m)
