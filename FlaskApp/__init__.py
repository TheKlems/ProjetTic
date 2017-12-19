# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import subprocess
import random

# create Flask app
app = Flask(__name__)

# define function for root url and return Hello World
@app.route('/')
def hello_world():
	returnvalue = {'funcname': 'test{0}'.format(random.randrange(4)), 'values':[random.randrange(33),random.randrange(33),random.randrange(33)]}
	return render_template('test.html', returnvalue = returnvalue)

@app.route('/mkdir')
def mkdir():

	#subprocess.Popen("sshpass -p 'tic2017' ssh -o StrictHostKeyChecking=no projettic@192.168.17.3 cd /home/projettic/Desktop/ && python3 -c 'from turnRight import *; turnRight(180)'", shell=True)
	subprocess.Popen("sshpass -p 'tic2017' ssh -o StrictHostKeyChecking=no projettic@192.168.17.3 \"cd /home/projettic/Desktop/ && python3 -c 'from turnRight import *; turnRight(180)'\"", shell=True)
	#subprocess.Popen("sshpass -p 'tic2017' ssh -o StrictHostKeyChecking=no projettic@192.168.17.3 python3 /home/projettic/PythonExamples/TestAllFunctions.py", shell=True)
	#p=subprocess.Popen("python3 /home/projettic/PythonExamples/TestAllFunctions.py", shell=True)
	#p=subprocess.Popen("mkdir /var/www/FlaskApp/FlaskApp/test", shell=True)
	return 'done'

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

# define function for /nextfunc url
@app.route('/nextfunc')
def nextfunc():
    # create return value with a func name (between func0 and func3) with led color value (red, green and blue between 0 and 32)
    returnvalue = {'funcname': 'test{0}'.format(random.randrange(4)), 'values':[random.randrange(33),random.randrange(33),random.randrange(33)]}
    # return returnvalue object in json
    return jsonify(returnvalue)

if __name__ == '__main__':
    app.run(debug=True)