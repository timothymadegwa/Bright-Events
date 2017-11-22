from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StingField, PasswoedField
from wtforms.validators import InputRequired, email, length
app= Flask(__name__)
app.config['SECERET_KEY']='THISISTHESECRETKEYFORTHEAPP'
Bootstrap(app)


@app.route('/')
def index