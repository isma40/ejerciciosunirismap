from flask import Flask, request, jsonify

app = Flask(__name__)  # Crear la instancia de Flask

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        result = num1 * num2
        return jsonify({"result": result}), 200
    except Exception:
        return jsonify({"error": "Invalid input"}), 400

@app.route('/divide', methods=['GET'])
def divide():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        if num2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 406
        result = num1 / num2
        return jsonify({"result": result}), 200
    except Exception:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)

