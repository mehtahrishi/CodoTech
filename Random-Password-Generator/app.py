import secrets
import string
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def generate_strong_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """
    Generates a secure, random password with guaranteed character types.
    """
    # Build the master character set based on user's choices
    alphabet = ""
    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_lowercase:
        alphabet += string.ascii_lowercase
    if use_numbers:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    # Fallback: If no character sets are selected, default to lowercase
    if not alphabet:
        alphabet = string.ascii_lowercase
        use_lowercase = True

    password_chars = []
    
    # --- Guarantee at least one of each selected character type ---
    if use_uppercase:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_numbers:
        password_chars.append(secrets.choice(string.digits))
    if use_symbols:
        password_chars.append(secrets.choice(string.punctuation))

    # --- Fill the rest of the password length with random chars from the combined alphabet ---
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(alphabet))

    # --- Shuffle the list to ensure character positions are random ---
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

# --- Page Routes ---
@app.route('/')
def index():
    initial_password = generate_strong_password(length=16, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True)
    return render_template('index.html', initial_password=initial_password)

# Other page routes remain the same
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/strong')
def strong():
    return render_template('strong.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

# --- API Endpoint ---
@app.route('/password')
def get_new_password():
    """API endpoint to fetch a new password based on all user options."""
    try:
        length = int(request.args.get('length', 16))
        if not 8 <= length <= 64:
            length = 16
    except (ValueError, TypeError):
        length = 16

    # Get boolean values from checkbox parameters
    use_uppercase = request.args.get('uppercase') == 'true'
    use_lowercase = request.args.get('lowercase') == 'true'
    use_numbers = request.args.get('numbers') == 'true'
    use_symbols = request.args.get('symbols') == 'true'

    new_password = generate_strong_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
    return jsonify({'password': new_password})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)