import flask
from flask import request, jsonify
import random
from random import randint

app = flask.Flask(__name__)
app.config["DEBUG"] = True

officelist = []
for i in range(100):
    officelist.append({'id':i,'busyness':"{0:.2f}".format(random.random())})


requestedid = [randint(0,2) for i in range(100)]

def customfunc(noofterms,left):
    sum = float(0)
    for i in range(noofterms):
        sum = sum + float((left/2)/(2**i))
    return sum-0.05


@app.route('/api/v1/officelist', methods=['GET'])
def api_id():
    if 'id' in request.args:
        listids = request.args['id'].split(' ')
        listids = [int(id) for id in listids]
    else:
        return "Error: No id field provided. Please specify an id."


    results = []

    for office in officelist:
        if office['id'] in listids:
            extrabusy = customfunc(int(requestedid[office['id']]),float(1.0-float(office['busyness'])))
            requestedid[office['id']] = requestedid[office['id']] + 1
            office['busyness'] = float(office['busyness']) + float("{0:.2f}".format(extrabusy))
            results.append(office)
            office['busyness'] = float(office['busyness']) + float("{0:.2f}".format(extrabusy))

    return jsonify(results)

app.run()
