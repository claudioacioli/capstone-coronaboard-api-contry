from flask import jsonify
from . import api as app_api
from .. import db
from ..models import Country


@app_api.route('/country', methods=['GET'])
def country():
    countries = Country.query.all()
    return jsonify([country.to_json() for country in countries])

