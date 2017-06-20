from flask import Flask, session

from petclinic.config import DevConfig

from flask import url_for, request
import jinja2


bundles = {
    }


# App init
app = Flask(__name__)
app.jinja_loader = jinja2.FileSystemLoader('templates')

app.config.from_object(DevConfig)
