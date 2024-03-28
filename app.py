from flask import Flask , request, send_file, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello():
    if request.method == 'GET':
        return send_file("./hello.html")
    elif request.method == 'POST':
        return "<h1>Hello POST</h1>"
    else:
         return"Error"

@app.route('/users/<id>',)
def users(id=None):
        return f"<h1>Im here {id}</h1>"

@app.route('/api',)
def api():
    reqUrl = "https://www.themealdb.com/api/json/v1/1/random.php"
    headersList = {
        "Accept": "*/*",
    }
    payload = ""
    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    cat = response.json()['meals'][0]['strCategory']

    if response.status_code == 200:
            return {
            "status": 200,
            "data": cat
        }

if __name__ == '__main__':
    app.run(debug=True, port=80)