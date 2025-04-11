from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from ai.matching import find_matches

app = Flask(__name__)
CORS(app)

STORIES_FILE = 'data/stories.json'

@app.route('/stories', methods=['POST'])
def submit_story():
    story = request.json.get('story')
    if not story:
        return jsonify({'error': 'Story is required'}), 400

    try:
        with open(STORIES_FILE, 'r+') as file:
            stories = json.load(file)
            stories.append({'id': len(stories) + 1, 'story': story})
            file.seek(0)
            json.dump(stories, file)
        return jsonify({'message': 'Story submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/match', methods=['POST'])
def match_stories():
    story = request.json.get('story')
    if not story:
        return jsonify({'error': 'Story is required'}), 400

    try:
        with open(STORIES_FILE, 'r') as file:
            stories = json.load(file)
        matches = find_matches(story, stories)
        return jsonify(matches), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
