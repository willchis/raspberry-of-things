from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = {}

@app.route('/')
def default_route():
    return "ok", 200

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        data_store['received_data'] = data
        
        return jsonify({'message': 'Data stored successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/data', methods=['GET'])
def return_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)
