from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def about():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get('name', '')
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

@app.route('/api/v1.0/predict')
def predict():
    num1 = request.args.get('num1', default=0, type=float)
    num2 = request.args.get('num2', default=0, type=float)
    
    prediction = 1 if (num1 + num2) > 5.8 else 0
    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == '__main__':
    app.run()
