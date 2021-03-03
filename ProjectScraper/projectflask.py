from flask import Flask
from flask import render_template
import projectscraper

website = Flask(__name__, template_folder="template")

namelist = projectscraper.scape_work("https://www.nzdirectory.co.nz/index.html")

@website.route('/')
def index():
    return render_template('index.html', namelist=namelist)



#      $env:FLASK_APP = "projectflask.py"