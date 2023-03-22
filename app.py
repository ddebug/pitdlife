from flask import Flask, render_template, request, redirect, url_for, flash
from models.player_model import Player
from models.activity_model import Activity
from api.player_api import PlayerAPI

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    players = Player.query.all()
    return render_template('index.html', players=players)

@app.route('/player/create', methods=['GET', 'POST'])
def create_player():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        major = request.form['major']
        player = Player(name=name, gender=gender, age=age, major=major)
        player.save()
        flash('Player created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create_player.html')

@app.route('/player/<int:player_id>')
def player_detail(player_id):
    player = Player.get(player_id)
    activities = Activity.get_by_player_id(player_id)
    return render_template('player_detail.html', player=player, activities=activities)

app.register_blueprint(PlayerAPI)

if __name__ == '__main__':
    app.run()
