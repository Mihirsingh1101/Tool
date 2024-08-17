from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    print("hello world")
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(debug=True)
