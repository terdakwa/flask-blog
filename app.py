from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1/27017")
db = client.flask_blog
blogs = db.blog

@app.route('/')
def page_index():
	return render_template('index.html')

@app.route('/about')
def page_about():
	return render_template('about.html')

@app.route('/blog')
def page_blog():
	blogs_l = blogs.find()
	return render_template('blog.html', blogs=blogs_l)

@app.route('/contact')
def page_contact():
	return render_template('contact.html')


if __name__ == "__main__":
	app.run(debug=True)
