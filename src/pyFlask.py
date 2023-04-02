from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Do something with name and email
    return 'Form submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
