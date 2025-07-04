from flask import Flask, request, jsonify
import random

app = Flask(__name__)

letters = [
    {"letter": "A", "value": 1, "strokes": 2, "vowel": True},
    {"letter": "B", "value": 2, "strokes": 1, "vowel": False}
]


def validate_username(username):
    if len(username) < 4 or not username.isalpha():
        return False

    username = username.lower()
    a = username.find('a')
    b = username.find('b', a + 1) if a != -1 else -1
    c = username.find('c', b + 1) if b != -1 else -1

    return c != -1


def shuffle(arr):
    result = arr[:]
    for i in range(len(result) - 1, 0, -1):
        j = random.randint(0, i)
        result[i], result[j] = result[j], result[i]
    return result


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username', '')
    password = data.get('password', '')

    if not validate_username(username) or password != username[::-1]:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"})


@app.route('/api/letters', methods=['GET'])
def list_letters():
    unique = {l["letter"]: l["value"] for l in letters}
    sorted_letters = sorted(unique.keys(), key=lambda x: unique[x])
    return jsonify({"letters": sorted_letters})


@app.route('/api/letter/add', methods=['POST'])
def add_letter():
    data = request.get_json() or {}

    try:
        letter = data['letter']
        value = data['value']
        strokes = data['strokes']
        vowel = data['vowel']

        # Check constraints
        if (any(l["letter"] == letter for l in letters) or
                strokes == value or
                not isinstance(value, int) or
                not isinstance(strokes, int) or
                not isinstance(vowel, bool)):
            return jsonify({"status": 1})

        letters.append({"letter": letter, "value": value, "strokes": strokes, "vowel": vowel})
        return jsonify({"status": 0})

    except (KeyError, TypeError):
        return jsonify({"status": 1})


@app.route('/api/letter/<string:letter>', methods=['GET'])
def get_letter(letter):
    for l in letters:
        if l["letter"] == letter:
            return jsonify(l)
    return jsonify({"error": "Letter not found"}), 404


@app.route('/api/letter/shuffle', methods=['GET'])
def shuffle_letters():
    unique_letters = list({l["letter"] for l in letters})
    return ''.join(shuffle(unique_letters))


@app.route('/api/letter/filter/<int:val>', methods=['GET'])
def filter_letters(val):
    filtered = [l["letter"] for l in letters if l["value"] <= val]
    return jsonify({"letters": filtered})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)