from flask import Flask, request, jsonify
from flask_cors import CORS
from ai.matching import process_story, find_matches
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data/stories.json')

@app.route('/submit_story', methods=['POST'])
def handle_submit():
    story_data = request.json
    if 'story' not in story_data or not story_data['story']:
        return jsonify({'error': 'Story is required'}), 400

    try:
        processed = process_story(story_data['story'])
        with open(DATA_FILE, 'r+') as f:
            stories = json.load(f)
            user_id = f"user{len(stories) + 1}"
            stories.append({
                "id": user_id,
                **processed,
                "story": story_data['story']
            })
            f.seek(0)
            json.dump(stories, f)
        return jsonify({"id": user_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_matches', methods=['GET'])
def handle_matches():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        with open(DATA_FILE, 'r') as f:
            stories = json.load(f)
        matches = find_matches(user_id, stories)
        return jsonify(matches), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', True))
