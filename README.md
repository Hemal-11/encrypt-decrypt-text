
## Caesar Cipher Flask App

This is a web application for basic encryption and decryption of text using the Caesar Cipher algorithm, built with Python and Flask.

### Features

- **Encrypt & Decrypt:** Easily encode or decode messages using a shift value (classic Caesar Cipher).
- **Favorites:** Save your favorite messages for quick access.
- **History:** View your recent encryption and decryption actions.
- **Modern UI:** Responsive design with dark/light mode toggle and animated logo.
- **AJAX Functionality:** Instant results without page reloads.
- **Customizable Shift:** Choose any shift value between 0 and 25.

### How It Works

- Enter your message and select a shift value.
- Click "Encrypt" to encode or "Decrypt" to decode.
- Your result appears instantly, and recent actions are tracked.
- You can save messages as favorites or clear the form.

### Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Algorithm:** Caesar Cipher (implemented in logic.py)

### Getting Started

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open in your browser: `http://localhost:5000`

### Folder Structure

- app.py — Main Flask application
- logic.py — Caesar Cipher algorithm
- index.html — Main HTML template
- style.css — Stylesheet

Also I have deployed this on the link: https://encrypt-decrypt-text.onrender.com/
