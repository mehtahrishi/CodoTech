# 🔐 Random Password Generator Web App

A secure, feature-rich password generator built with **Python (Flask)** and a stunning **Glassmorphic UI**. Generate strong, customizable passwords that automatically refresh every 10 seconds, complete with a visual countdown timer! ✨

## 🧰 Key Features

* ✅ **Secure Password Generation**: Uses Python's `secrets` module for cryptographically strong randomness.
* 🎛️ **Fully Customizable**:
    * **Password Length**: Adjust the length from 8 to 64 characters with a smooth slider.
    * **Character Types**: Use checkboxes to include/exclude uppercase, lowercase, numbers, and symbols.
    * **Guaranteed Characters**: The backend ensures at least one character from each selected category is included.
* 🔁 **Auto-Refresh with Visual Timer**:
    * Fetches a new password every 10 seconds without reloading the page.
    * A 10-dot visual timer shows the countdown to the next refresh.
* 📋 **Copy to Clipboard**: Easily copy the generated password with a single click and visual feedback.
* 🌈 **Modern Glassmorphism UI**: A beautiful, blurred, frosted-glass interface built with pure CSS.
* 📱 **Fully Responsive**: Looks and works great on desktops, tablets, and mobile devices.
* ℹ️ **Informational Pages**: Includes "What Makes a Password Strong?", "About", and "FAQ" pages.
* 💡 **Lightweight & Fast**: No heavy frameworks, just pure HTML, CSS, JS, and Flask.

---

## 🛠️ Tech Stack

| Layer    | Technology                      |
| -------- | ------------------------------- |
| Frontend | HTML, CSS (Glassmorphism), JS   |
| Backend  | Python + Flask                  |
| Security | Python `secrets` module         |
| Hosting  | Run locally or on Replit/Render |

---

## 🗂️ Folder Structure

```

password-generator/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
└── templates/
├── base.html
├── index.html
├── about.html
├── strong.html
└── faq.html

````

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone [https://github.com/mehtahrishi/Random-Password-Generator.git](https://github.com/mehtahrishi/Random-Password-Generator.git)
cd Random-Password-Generator
````

### 2\. Set Up a Virtual Environment (Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4\. Run the Flask App

```bash
python app.py
```

### 5\. Open in Your Browser

Visit `http://127.0.0.1:5000` to see the app live\!

-----

## 🤔 How It Works

**Backend (`app.py`):**

  * A Flask server handles all routing.
  * The `/password` API endpoint accepts parameters for length and character types (uppercase, lowercase, numbers, symbols).
  * The `generate_strong_password()` function intelligently builds a character set based on the user's choices, guarantees at least one character from each selected type, fills the remaining length, and securely shuffles the result.

**Frontend (`index.html` & JS):**

  * Event listeners on the slider and checkboxes trigger a refresh whenever an option is changed.
  * A `setInterval` function calls the `fetchNewPassword()` function every 10 seconds.
  * The `fetchNewPassword()` function constructs a URL with the current settings (e.g., `/password?length=20&uppercase=true...`) and requests a new password from the Flask API.
  * The UI is dynamically updated with the new password, a fade animation, and a reset of the visual dot timer.

-----

## ✨ Future Ideas

  * 🎨 **Dark/Light Mode Toggle**: Allow users to switch between visual themes.
  * 📊 **Password Strength Meter**: Provide real-time feedback on the strength of the chosen options.
  * 📱 **Progressive Web App (PWA)**: Make the app installable on mobile and desktop devices.
  * 🔐 **User Accounts**: Allow users to sign in and save password generation history (would require a database).

-----

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.

-----

## 🤝 Credits

Created with ❤️ by Hrishi Mehta. Inspired by modern UI/UX design trends.

```
```
