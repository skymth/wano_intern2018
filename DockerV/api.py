from flask import Flask, jsonify, abort, make_response
from peewee import *

database = MySQLDatabase('skymth_db', **{'charset': 'utf8', 'use_unicode': True, 'host': 'mysql', 'port': 3306, 'user': 'skymth_user', 'password': 'skymth_pass'})
#database = MySQLDatabase('skymth_db', **{'charset': 'utf8', 'use_unicode': True, 'host': 'mysql', 'port': 3306, 'user': 'skymth_user', 'password': 'skymth_pass'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class WanoIntern(BaseModel):
    artist = IntegerField(column_name='artist_id')
    country = IntegerField(column_name='country_id')
    create_time = DateTimeField()
    distribution_type = IntegerField()
    id = BigIntegerField()
    jpy_total_price = CharField(constraints=[SQL("DEFAULT 0.00000000000000000000")])
    jpy_unit_price = CharField(constraints=[SQL("DEFAULT 0.00000000000000000000")])
    release = IntegerField(column_name='release_id')
    report_date = DateField()
    song = IntegerField(column_name='song_id', null=True)
    store = IntegerField(column_name='store_id')
    total_quantity = IntegerField()
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'wano_intern'
        indexes = (
            (('id', 'report_date'), True),
        )
        primary_key = CompositeKey('id', 'report_date')


api = Flask(__name__)

@api.route('/getWanoIntern/<string:id>', methods=['GET'])
def get_user(id):
    try:
        wanointern = WanoIntern.get(WanoIntern.id == id)
    except WanoIntern.DoesNotExist:
        abort(404)

    result = {
        "result":True,
        "data":{
            'id' : wanointern.id,
            'create_time' : wanointern.create_time,
            'update_time' : wanointern.update_time,
            'report_date' : wanointern.report_date,
            'store_id' : wanointern.store,
            'country_id' : wanointern.country,
            'artist_id' : wanointern.artist,
            'release_id' : wanointern.release,
            'song_id' : wanointern.song,
            'distribution_type' : wanointern.distribution_type,
            'total_quantity' : wanointern.total_quantity,
            'jpy_unit_price' : wanointern.jpy_unit_price,
            'jpy_total_price' : wanointern.jpy_total_price,
            }
        }

    return make_response(jsonify(result))

@api.route('/getArtist/<string:artist_id>', methods=['GET'])
def get_Artist(artist_id):
    try:
        query = WanoIntern.select().where(WanoIntern.artist ==artist_id)
    except WanoIntern.DoesNotExist:
        abort(404)

    sum = 0
    for wanointern in query:
        artist = wanointern.artist
        sum += float(wanointern.jpy_total_price)

    result = {
        "result":True,
        "data":{
            'artist_id' : wanointern.artist,
            'total_sales' : sum,
            }
        }

    return make_response(jsonify(result))

@api.route('/getArtist/country/<string:artist_id>', methods=['GET'])
def get_country(artist_id):
    try:
        query = WanoIntern.select().where(WanoIntern.artist ==artist_id)
    except WanoIntern.DoesNotExist:
        abort(404)

    country_li = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}
    for wanointern in query:
        artist = wanointern.artist
        if wanointern.country == 0:
            country_li[wanointern.country] += float(wanointern.jpy_total_price)
        elif wanointern.country == 1:
            country_li[wanointern.country] += float(wanointern.jpy_total_price)

        elif wanointern.country == 2:
            country_li[wanointern.country] += float(wanointern.jpy_total_price)

        elif wanointern.country == 3:
            country_li[wanointern.country] += float(wanointern.jpy_total_price)

        elif wanointern.country == 4:
            country_li[wanointern.country] += float(wanointern.jpy_total_price)

        elif wanointern.country == 5:
            country_li[wanointern.country] += float(wanointern.jpy_total_price)


    result = {
        "result":True,
        "data":{
            'artist_id' : wanointern.artist,
            'US' : country_li[0],
            'UK' : country_li[1],
            'JP' : country_li[2],
            'CN' : country_li[3],
            'RU' : country_li[4],
            'UGANDA' : country_li[5]
            }
        }

    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
