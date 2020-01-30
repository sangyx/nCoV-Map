from flask import Flask, render_template, jsonify
from datetime import timedelta
from logistic import update_map, update_news, update_overall, confirmed_map

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map")
def get_map():
    map_data = update_map()
    return confirmed_map(map_data).dump_options_with_quotes()


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
