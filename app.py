from flask import Flask, render_template, request, redirect, flash, session, make_response, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import conversion

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = '12345'
# debug = DebugToolbarExtension(app)

@app.route('/')
def main():
    """
    Presents the main page form with any error messages
    """
    return render_template('home.html')

@app.route('/results')
def result():
    """
    Presents conversion results
    """
    cur_from = request.args.get('from',None)
    cur_to = request.args.get('to',None)
    amount = request.args.get('amount',None)
    result = conversion.convert(cur_from,cur_to,amount)
    if isinstance(result,list):
        for err in result:
            flash(err)
        return redirect('/')
    return render_template('results.html',results = result)