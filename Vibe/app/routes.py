# app/routes.py (Definitive Final Version)

from flask import Blueprint, render_template, json
import pandas as pd

main_bp = Blueprint('main_bp', __name__)

# Load the song library once when the app starts
try:
    song_library_df = pd.read_csv('data/song_library.csv', quotechar='"')
    # Convert the DataFrame to a standard Python list of dictionaries
    song_library_list = song_library_df.to_dict(orient='records')
except FileNotFoundError:
    print("FATAL: data/song_library.csv not found!")
    song_library_list = []

@main_bp.route('/')
def index():
    """Serves the main page and injects the song library directly."""
    users = ['user_01', 'user_02', 'user_03', 'new_user'] # This is just for display, can be removed
    
    # Pass the raw Python list to the template.
    # The 'tojson' filter in the template will handle the conversion.
    return render_template('index.html', song_library=song_library_list, users=users)