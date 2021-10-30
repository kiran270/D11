from flask import Flask, render_template, request
import json
from google.cloud import datastore
datastore_client = datastore.Client()
app = Flask(__name__)

def adddreamteam(matchbetween,stadium,pitchtype,fav,one,two,three,four,five,six,seven,eight,nine,ten,eleven):
    entity = datastore.Entity(key=datastore_client.key('matches'))
    entity.update({
        "matchbetween":matchbetween,
        "stadium":stadium,
        "pitchtype":pitchtype,
        "fav":fav,
        "one":one,
        "two":two,
        "three":three,
        "four":four,
        "five":five,
        "six":six,
        "seven":seven,
        "eight":eight,
        "nine":nine,
        "ten":ten,
        "eleven":eleven
    })
    datastore_client.put(entity)

def filter_matchs(filteroptions):
    query = datastore_client.query(kind='matches')
    for x in filteroptions:
        query.add_filter(x, "=", filteroptions[x])
    matches = list(query.fetch())
    return matches

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/adddreamteam',methods = ["POST"])
def adddreamtem():
    matchbetween=request.form.get("matchbetween")
    stadium=request.form.get("stadium")
    pitchtype=request.form.get("pitchtype")
    fav=request.form.get("fav")
    one=request.form.get("1")
    two=request.form.get("2")
    three=request.form.get("3")
    four=request.form.get("4")
    five=request.form.get("5")
    six=request.form.get("6")
    seven=request.form.get("7")
    eight=request.form.get("8")
    nine=request.form.get("9")
    ten=request.form.get("10")
    eleven=request.form.get("11")
    adddreamteam(matchbetween,stadium,pitchtype,fav,one,two,three,four,five,six,seven,eight,nine,ten,eleven)
    return render_template('index.html')
@app.route('/getdreamteams',methods = ["POST"])
def getdreamtem():
    pitchtype=request.form.get("pitchtype")
    fav=request.form.get("fav")
    x={}
    x["pitchtype"]=pitchtype
    x["fav"]=fav
    res = filter_matchs(x)
    return render_template('dreamteams.html',data=res)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
