from flask import Flask
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    return 'sometimes gonna Think about you'

if __name__ == '__main__':
    app.run(debug=True)
