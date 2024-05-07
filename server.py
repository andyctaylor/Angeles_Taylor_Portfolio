# I imported flask, render template for html files
from flask import Flask, render_template, send_file, request

# importing the CSV Module 
import csv

# I started an instance of the app
app = Flask(__name__, static_folder='static')


# I set the default home route using a decorator.
@app.route('/')
def home():
    return render_template('index.html')


# Accept stage parameters and creates route dynamically for each page.
@app.route('/<page_name>')
def dynamic_page(page_name):
  return render_template(page_name)

# Downloads my CV.
@app.route('/download_cv')
def download_cv():
   path_to_cv = '/static/documents/Andy_Taylor_CV_2024_TB.pdf'
   return send_file(path_to_cv, as_attachment=True, attachment_filename='Andy_Taylor_CV_2024_TB.pdf')


#  This will open my temporary database file (database.txt) 
def write_to_database(data):
       with open('./database/database.txt', 'a') as database: # append the new data to the database file
            name = data["name"]
            subject = data["subject"]
            email = data["email"]
            message = data["message"]
            file = database.write(f'\n\n You have received a new message today:\n{name} \n{subject} \n{email} \n{message}')

#  This will open my temporary database file (database.csv) 
def write_to_database_csv(data):
       with open('./database/database.csv',  newline='', mode='a') as database_csv: # append the new data to the database file
            name = data["name"]
            subject = data["subject"]
            email = data["email"]
            message = data["message"]

            # writing this info to database_csv
            csv_writter = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writter.writerow([name,subject,email,message])


# This is for my contact form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_from():
    # Logic for saving the data I received from my form to my database.
    if request.method == 'POST':
       try:
        # Turning all of my form data into a dictionary object.
        data = request.form.to_dict()
        # Using the function right to database.
        write_to_database_csv(data)
        
          # This will return the success page after a successful form submission.
        return render_template('success.html')
       except:
           return "Information was not saved to database"
    else:
       print('Something failed')



# Explicitly run with debug mode
if __name__ == '__main__':
    app.run(debug=True) 