from flask import Flask, render_template, request
import json
app = Flask(__name__)



def write_json(new_data, filename='results.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["matches"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def filter_json(fav,pitchtype, filename='results.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        print(file_data)
        print(fav)
        print(pitchtype)
        if fav != "None" and pitchtype!="None":
            output_dict = [x for x in file_data['matches'] if x['pitchtype'] == pitchtype and x['fav'] == fav]
            return output_dict
        if fav != "None" and pitchtype == "None":
            print(".....")
            output_dict = [x for x in file_data['matches'] if  x['fav'] == fav]
            return output_dict
        if fav == "None" and pitchtype!= "None":
            print("...")
            output_dict = [x for x in file_data['matches'] if x['pitchtype'] == pitchtype ]
            return output_dict


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/adddreamteam',methods = ["POST"])
def adddreamtem():
    matchbetween=request.form.get("matchbetween")
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
    data={
    "matchbetween":matchbetween,
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
    }
    write_json(data)
    return render_template('index.html')
@app.route('/getdreamteams',methods = ["POST"])
def getdreamtem():
    pitchtype=request.form.get("pitchtype")
    fav=request.form.get("fav")
    res = filter_json(fav,pitchtype)
    print(res)
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
