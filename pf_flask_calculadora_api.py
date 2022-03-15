from flask import Flask, render_template  
from flask import jsonify

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template('hello.html')
    
@app.route('/suma/',defaults={'x': 1,'y':1})
@app.route('/suma/<int:x>/<int:y>/',  methods = ['GET'])
def math(x, y):
    result = x + y # Sum x,t -> result
    response = '%d + %d = %d' %(x, y, result) #Buld response
    return response #Return response

@app.route('/resta/',defaults={'x': 1,'y':1})
@app.route('/resta/<int:x>/<int:y>/',  methods = ['GET'])
def math2(x, y):
    result = x - y # Sum x,t -> result
    response = '%d - %d = %d' %(x, y, result) #Buld response
    return response #Return response

@app.route('/mult/',defaults={'x': 1,'y':1})
@app.route('/mult/<int:x>/<int:y>/',  methods = ['GET'])
def math3(x, y):
    result = x * y # Sum x,t -> result
    response = '%d * %d = %d' %(x, y, result) #Buld response
    return response #Return response

@app.route('/div/',defaults={'x': 1,'y':1})
@app.route('/div/<int:x>/<int:y>/',  methods = ['GET'])
def math4(x, y):
    if y==0:
        response = 'No se puede dividir por cero'
        return response

    else:
        result = x / y# Sum x,t -> result
        response = '%d / %d = %d' %(x, y, result) #Buld response
        return response #Return response
        

@app.route('/mathapijson/<int:x>/<int:y>/', methods = ['GET'])
def mathjs(x, y):
    result = x + y #Sum x,t -> result
    data = {'x'  : x, 'y' : y, 'result' : result} #Buld arrary
    response = jsonify(data) #Convert to json
    response.status_code = 200 #Set status code to 200=ok
    response.headers['Link'] = 'http://localhost'

    return response #return json response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)