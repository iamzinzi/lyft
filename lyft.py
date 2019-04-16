#!/usr/bin/python3
"""Small web application in Python for Lyft Software Engineering
Apprenticeship Application"""
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/test', methods=['POST'], strict_slashes=False)
def every_third_letter():
    """Accepts one argument 'string_to_cut', creates a new string using every
    third letter from the original string, and returns it in JSON format."""
    string_to_cut = request.get_json(silent=True)['string_to_cut']
    new_string = ''
    for i in range(1, len(string_to_cut) + 1):
        if i % 3 == 0:
            new_string += string_to_cut[i - 1]
    retval = {'return_string': new_string}
    return jsonify(retval)

if __name__ == '__main__':
    app.run()
