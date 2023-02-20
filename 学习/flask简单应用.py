from flask import Flask,jsonify,request
from wsgiref.simple_server import make_server

app = Flask(__name__)
@app.route('/',methods=['post','get'])
def index():
    name = request.args.get('name')
    if name:
        return f'你的名字是{name}'
    with open('q.html','r',encoding='utf-8') as f:
        a = f.read()
        return a
   # return jsonify({'name':'zwj','age':88})

srv = make_server('0.0.0.0',5000,app)
srv.serve_forever()
# app.run()