from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World'

@app.route('/aboutUs')
def aboutUs():
    return 'this is about us page'

@app.route('/contactUs', methods=['POST'])
def contactUs():
    return 'this is contact us page'

if __name__ == '__main__':
    app.run(port=3001, debug=True)