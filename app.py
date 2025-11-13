# app.py
import connexion
from flask import render_template

app = connexion.App(__name__, specification_dir='.')
app.add_api('openapi.yaml')

# Normal Flask routes for the web pages
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
