from flask import Flask, request, json, jsonify
from samsungcheck import search

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route('/search')
def index():
    username = request.args.get('username')
    if not username:
        return jsonify({'error': 'invalid username'})
    result = search(username)
    response = app.response_class(
        response=json.dumps(result, indent=2, ensure_ascii=False).encode('utf8'),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')