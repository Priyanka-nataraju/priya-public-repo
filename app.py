from flask import Flask 
import socket, json 

app = Flask(__name__)

@app.route('/')
def print_ip():
    hostname = socket.gethostname()
    get_ip = socket.gethostbyname(hostname)
    return get_ip
  
@app.route('/health')
def health_check():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/name')
def print_name():
    return 'Harsha Jain'

@app.route('/error')
def print_error():
    print('500 error')
    sum = 0/100
    return sum

if __name__ == '__main__':
  app.run(host="0.0.0.0", port="8080")
