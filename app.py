from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Bienvenue"


@app.route('/autre_chose')
def hello():
    return "Il fait beau"

if __name__ == '__main__':
    app.run(host='0.0.0.0')