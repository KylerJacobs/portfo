from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
from flask import send_from_directory

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/download_resume')
def download_resume():
    return send_from_directory('./static/assets/Resume_6_20_23.pdf', as_attachment=True)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('thankyou.html')
    else:
    	return 'someting went wrong, try again'