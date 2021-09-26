from flask import Flask
from flask.json import jsonify
from flask import request
from flask_cors import cross_origin
from utils.api import get_recommended_games, get_image_search_data, save_liked_games, get_liked_games

app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
@cross_origin()
def get_recommendation():
    game_ids = request.form.getlist('game_id')
    games = get_recommended_games(game_ids)
    return jsonify({'games': games, 'length': len(games)})


@app.route('/image_search', methods=['GET'])
@cross_origin()
def get_image_search():
    url = request.args.get('image_url')
    image_data = get_image_search_data(url)
    return jsonify(image_data)


@app.route('/like', methods=['POST'])
@cross_origin()
def like_game():
    _id = request.form.get('id')
    name = request.form.get('name')
    rating = request.form.get('rating')
    date = request.form.get('date')
    save_liked_games(_id, name, rating, date)
    return jsonify({'status': True, 'message': 'Added to the saved list'})


@app.route('/like', methods=['GET'])
@cross_origin()
def fetch_liked_games():
    games = get_liked_games()
    return jsonify(games)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
