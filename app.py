from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def save_state():
    return jsonify({
        "response": "good"
    })


@app.route('/send', method=['GET', 'POST'])
def route():
    if request.method == 'GET':
        # Handle GET request
        query_param = request.args.get('param_name')
        return f"Received GET request with parameter: {query_param}"
    elif request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        return f"Received POST request with data: {data}"


if __name__ == '__main__':
    app.run(debug=True)
