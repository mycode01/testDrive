from flask_restful import Resource
from flask import jsonify
from database import db_session as cfs, db_session2 as cfs2
from models import api_key, t_fund_items


class Keys(Resource):
    def get(self):
        queries = cfs.query(api_key)
        entries = [dict(seq=m.seq, auth_key=m.auth_key, ip4=m.ip4(), type=m.type, user_info=m.user_info) for m in
                   queries]
        return jsonify(keys=entries)


class Funds(Resource):
    def get(self):
        q = cfs2.query(t_fund_items).filter(t_fund_items.status == "2")
        e = [dict(title=m.title, fundsid=m.fundsID, status=m.status, targetAmt=m.targetAmount) for m in q]
        return jsonify(e)

