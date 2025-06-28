from flask import Blueprint, render_template
import pandas as pd
import os

main_bp = Blueprint('main_bp', __name__)

# Load song data from CSV
try:
    song_library_df = pd.read_csv(os.path.join("data", "song_library.csv"), quotechar='"')
    song_library_list = song_library_df.to_dict(orient='records')
except FileNotFoundError:
    print("\u274c ERROR: 'data/song_library.csv' not found!")
    song_library_list = []

@main_bp.route("/")
def index():
    print("Current working dir:", os.getcwd())
    print("Template exists:", os.path.exists("templates/index.html"))
    return render_template("index.html", song_library=song_library_list)