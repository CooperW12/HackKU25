from flask import Flask, request, jsonify
from DSPrompter import DSPrompter

app = Flask(__name__)
dsp = DSPrompter()

def read_file_skip_errors(file_path, encoding='utf-8'): #encoding errors from html >:(
    try:
        with open(file_path, 'r', encoding=encoding, errors='replace') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

@app.route('/')
def test_good():
    return jsonify({"response": "good"})


@app.route('/test')
def test():
    test_instruct = {
        "htmlCode": read_file_skip_errors("message.txt"),
        "instruction": "I want to go to my data structures and algorithms class"
    }

    json_response = dsp.get_json_response_from_dict_instruction(test_instruct)
    print("type:")
    print(type(json_response))
    print(json_response)

    return jsonify(json_response)


@app.route('/send', methods=['GET', 'POST'])
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


