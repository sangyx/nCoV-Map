from flask import Flask, render_template, jsonify
from datetime import timedelta
from logistic import update_news, update_overall, update_map, confirmed_map
from charts import gen_map
from get_data import gen_datapair_by_prov, repair_name

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/loading.gif')
def gif():
    with open('loading.gif', 'rb')as f:
         gif = f.read()


    return gif


@app.route("/map")
def get_map():
    map_data = update_map()
    return confirmed_map(map_data).dump_options_with_quotes()
    # return gen_map("china", gen_datapair_by_name()).dump_options_with_quotes()


@app.route("/pmap/<proName>")
def get_pmap(proName):
    return gen_map(proName, gen_datapair_by_prov(repair_name(proName)))


@app.route("/news")
def get_news():
    news = update_news()
    return jsonify(news)


@app.route("/overall")
def get_overall():
    overall = update_overall()
    return jsonify(overall)


if __name__ == "__main__":
     app.run(debug=True)
