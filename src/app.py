# Import necessary modules
from flask import Flask, render_template, request
from subprocess import Popen

# Create a Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')  # Serve the front-end HTML file

@app.route('/start', methods=['POST'])
def start_controller():
    # Start the gesture controller
    # Use subprocess to run your Python script
    # Replace 'path/to/your/python/script.py' with the actual path to your Python script
    Popen(['python', 'path/to/your/python/script.py'])
    return 'Gesture Controller started'

@app.route('/stop', methods=['POST'])
def stop_controller():
    # Stop the gesture controller
    # Your implementation to stop the gesture controller (if applicable)
    return 'Gesture Controller stopped'

@app.route('/exit', methods=['POST'])
def exit_controller():
    # Exit the application
    # Your implementation to exit the application (if applicable)
    return 'Application exited'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development purposes
