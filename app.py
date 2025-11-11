from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/<int:num>', methods=['GET'])
def calcular(num):
    factorial = math.factorial(num)
    if num % 2 == 0:
        etiqueta = "par"
    else:
        etiqueta = "impar"
    return jsonify({
        "Numero": num,
        "Factorial": factorial,
        "Etiqueta": etiqueta
    })

if __name__ == '__main__':
    app.run(debug=True)


