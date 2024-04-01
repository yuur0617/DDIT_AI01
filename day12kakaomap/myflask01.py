from flask import Flask, redirect, jsonify
from flask.globals import request
from flask.templating import render_template
import pymysql
from day12kakaomap.dao_bus_path import DaoBusPath


app = Flask(__name__)

@app.route('/')
def index():
    return redirect('static/bus_deajeon.html')
    
@app.route('/bp_list',methods=['POST'])
def emp_list():
    dbp = DaoBusPath()
    list = dbp.selectList()
    # print(list)
    return jsonify(list = list) 

@app.route('/bus')
def bus():
    return render_template("bus.html")

if __name__ == '__main__':
    app.run(debug=True)