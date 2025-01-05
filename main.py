from flask import Flask
app = Flask(_name_)

@app.route("/")
 def home():
   return "hello"

@app.route("/about")
 def about():
   return "hello about"
