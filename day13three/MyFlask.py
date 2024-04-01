from flask import Flask, redirect, jsonify, request
import pymysql

app = Flask(__name__)

@app.route('/')
def index():    
    return redirect('static\examples\_ex05.html')

if __name__ =='__main__' :
    app.run(debug=True)
    