from app import app
import json

from flask import render_template

todolist = [
		{'description': 'Walk the cat'},
		{'description': 'Win Nobel Prize'}
			]

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', todolist = todolist, myname = 'Jacqueline'.upper())

@app.route("/item")
def getItems():
	return json.dumps(todolist)

@app.route("/item/new", method="POST")
def additem():
	description = request.form["description"]
	todolist.append({"description": description})
	report  = {"status": success}
	return report