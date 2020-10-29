from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)
with open ('data.json')as json_file:
  jsonfile = json.load(json_file)

def mensaje():
  mensaje = 'hola desde el medotodo'
  return "alert('" + mensaje + "')"

@app.route('/')
def index():
  template = env.get_template('index.html')
  return template.render(my_data = jsonfile['data'], headers = jsonfile['headers'])

@app.route('/Create', methods = ['GET', 'POST'])
def crear():
  if request.method == 'POST':
    idnumber = request.form['id']
    Class = request.form['type']
    name = request.form['name']
    image = request.form['image']
    thumbnail = request.form['thumbnail']
    print (f'{idnumber} {Class} {name} {image} {thumbnail}')

    jsonfile['data'].append({"id":idnumber, "type":Class, "name":name, "image":{"url":image}, "thumbnail":{"url":thumbnail}})
    return redirect(url_for('index'))
  template = env.get_template('form.html')
  return template.render()

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)