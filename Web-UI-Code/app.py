from flask import Flask, render_template, request
app = Flask(__name__)
from recommendor import recommend_patents
import pandas as pd
import numpy as np

@app.route("/")
def index():
    return render_template("profile.html")


@app.route("/getRecommendations", methods=['POST'])
def profile():
       input_user = request.form['input']
       search_by = request.form['searchBy']
       noOfRows = request.form['noOfRows']
       result = recommend_patents(input_user, search_by, noOfRows)
       try:
              return render_template("results.html", tables=[result.to_html(classes='data')], titles=result.columns.values)
       except:
              return render_template("exception.html", message='Dataset does not contain any patents similar to your inputs')


if __name__ == "__main__":
    app.run()

