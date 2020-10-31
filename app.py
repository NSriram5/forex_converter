from flask import Flask, render_template, request, redirect, flash, session, make_response, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from forex_python.converter import CurrencyRates, CurrencyCodes

currency_symbols = CurrencyCodes()
currency_rates = CurrencyRates()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '12345'
debug = DebugToolbarExtension(app)


@app.route('/')
def main():
    return render_template('home.html')

@app.route('/results')
def result():
    return render_template('home.html')

# @app.route('/')
# def main_display():

#     board = None
#     board = session.get('board',None)
#     play_count = session.get('count',0)
#     highscore = session.get('highscore',0)
#     if board == None:
#         return render_template('main_screen.html',game_time = False,non_game_time = True, board_game = [],count = play_count, highscore = highscore)
#     return render_template('main_screen.html',game_time = True, non_game_time = False, board_game = board, count = play_count, highscore = highscore)

# @app.route('/check')
# def check_word_request():
#     word = request.args['q']
#     board = session['board']

#     valid = boggle_game.check_valid_word(board,word)
#     reply = {'results':valid}
#     return jsonify(reply)

# @app.route('/generate_board',methods = ['POST'])
# def make_board():
#     session['board'] = boggle_game.make_board()
#     return redirect('/')

# @app.route('/updatestats',methods = ['POST'])
# def update_stats():
#     play_count = session.get('count',0)
#     highscore = session.get('highscore',0)
#     play_count += 1
#     if int(request.get_json()['playerscore'])> highscore:
#         highscore = int(request.get_json()['playerscore'])
#     session['highscore'] = highscore
#     session['count'] = play_count
#     return jsonify({'playcount':play_count,'highscore':highscore})