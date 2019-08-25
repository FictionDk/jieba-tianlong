# -*- coding: utf-8 -*-
from flask import Flask,jsonify
import jiebalong

app = Flask(__name__)

@app.route('/long/frequencies/person',methods=['GET'])
def persons_frequency():
    seriesData = jiebalong.read_result()
    legendData = []
    selected = {}
    for val in seriesData:
        legendData.append(val["name"])
        selected[val["name"]] = True

    result = {}
    result["seriesData"] = seriesData
    result["legendData"] = legendData
    result["selected"] = selected
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=10001)
