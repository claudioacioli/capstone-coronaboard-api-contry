from . import db


class Country(db.Model):

    __tablename__ = 'countries'
    
    country_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cases = db.Column(db.BigInteger, default=0, nullable=False)
    today_cases = db.Column(db.Integer, default=0, nullable=False)
    deaths = db.Column(db.Integer, default=0, nullable=False)
    today_deaths = db.Column(db.Integer, default=0, nullable=False)
    critical = db.Column(db.Integer, default=0, nullable=False)
    flag = db.Column(db.String(1000))

    def to_json(self):
        return {
            'countryId': self.country_id, \
            'name': self.name, \
            'cases': self.cases, \
            'todayCases': self.today_cases, \
            'deaths': self.deaths, \
            'todayDeaths': self.today_deaths, \
            'critical': self.critical, \
            'flag': self.flag \
        }

    def __repr__(self):
        return '<Country %r>' %self.name

