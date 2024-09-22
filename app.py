from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page with feedback form
@app.route('/')
def index():
    return render_template('index.html')

# Handling form submission and displaying thank you message
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        feedback = request.form['feedback']
        
        # Check if the form is filled
        if name == '' or feedback == '':
            return 'Please fill out the form!'
        
        # Redirect to the thank you page with name and feedback
        return render_template('thankyou.html', name=name, feedback=feedback)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)    
