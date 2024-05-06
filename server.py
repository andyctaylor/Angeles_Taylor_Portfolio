# I imported flask, render template for html files
from flask import Flask, render_template, send_file

# I started an instance of the app
app = Flask(__name__, static_folder='static')

# I set the default home route using a decorator.
@app.route('/')
def home():
    return render_template('index.html')

# Downloads my CV.
@app.route('/download_cv')
def download_cv():
   path_to_cv = '/static/documents/Andy_Taylor_CV_2024_TB.pdf'
   return send_file(path_to_cv, as_attachment=True, attachment_filename='Andy_Taylor_CV_2024_TB.pdf')