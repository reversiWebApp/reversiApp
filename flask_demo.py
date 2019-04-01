import sqlite3

from flask import Flask
from flask import render_template
from flask import request
from flask import g

from reversiTools.web_app_reversi_tools import intlist2string
from reversiTools.web_app_reversi_tools import string2intlist
from reversiTools.web_app_reversi_tools import list2matrix
from reversiTools.web_app_reversi_tools import matrix2list
from reversiTools.web_app_reversi_tools import get_simple_board
from reversiTools.web_app_reversi_tools import get_initial_status
from reversiTools.web_app_reversi_tools import step
from sqlite3_commands import CREATE_PLAYER_NAME_TABLE
from sqlite3_commands import REGISTER_PLAYER_WHITE_NAME 
from sqlite3_commands import GET_PLAYER_WHITE_NAME
from sqlite3_commands import REGISTER_PLAYER_BLACK_NAME
from sqlite3_commands import GET_PLAYER_BLACK_NAME
from sqlite3_commands import CREATE_BOARD_INFO_TABLE
from sqlite3_commands import REGISTER_BOARD_INFO
from sqlite3_commands import GET_BOARD_INFO
from sqlite3_commands import UPDATE_BOARD_INFO 

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('game_info.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/', methods=["GET", "POST"])
def home():
    # db = get_db()
    # curs = db.cursor()
    # cursor.exexute()
    return render_template('home.html')

@app.route('/mode_select/', methods=["GET", "POST"])
def mode_select(username=None):
    username = request.values['username']
    return render_template('mode_select.html')

@app.route('/game/dqn/<index>/', methods=["GET", "POST"])
def dqn():
    return render_template('dqn.html', username=username)


@app.route('/fin/', methods=["GET"])
def fin():
    return render_template('fin.html', winner="いより")


def _main():
    app.run(debug=True)

if __name__ == '__main__':
    _main()
