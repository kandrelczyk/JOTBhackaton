from sqlalchemy import create_engine
from sqlalchemy import text
import urllib.request
import json

r = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/forecast?lat=51.5&lon=0&appid=fa691aaeb8b8e8e0fdfc3c9c74e56620")

data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

main = data['list'][1]['main']

engine = create_engine("iris://SQLAdmin:Password2023!@k8s-99982284-a1cd6c37-2fa44f5f14-79b56ba4edd0e5e8.elb.eu-central-1.amazonaws.com:1972/USER")

with engine.connect() as con:

    rs = con.execute(text('SELECT PREDICT(noRadiation use testNoRadiation with (11, 5, 12, {}, 60, {}, {}, {})) as prediction'.format(data['list'][1]['wind']['speed'], main['pressure'], main['feels_like'], main['humidity'])))

    print('Running query: SELECT PREDICT(noRadiation use testNoRadiation with (11, 5, 12, {}, 60, {}, {}, {})) as prediction'.format(data['list'][1]['wind']['speed'], main['pressure'], main['feels_like'], main['humidity']))

    for row in rs:
        print("Predited power generation: {}".format(row))