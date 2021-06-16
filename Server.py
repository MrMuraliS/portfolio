from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def home_return(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./database.txt', 'a') as database:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('./database.csv', newline='', mode='a') as database2:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        write_csv = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_csv.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong, try agian!'
