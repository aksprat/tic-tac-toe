from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    # Get the value of the clicked button (either 'X' or 'O')
    player_choice = request.form['player_choice']
    # Process the game logic here (not implemented in this example)
    # For simplicity, we just return a message indicating the chosen option
    return f"You chose: {player_choice}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
