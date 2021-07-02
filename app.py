from flask import Flask, render_template
from flask_caching import Cache
from helpers import run


# Flask-Caching related configs
config = {
    "CACHE_TYPE": "SimpleCache",  
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)


@app.route("/")
@cache.cached(timeout=50)
def index():
    text, age = run()
    return render_template('index.html', age=age, text=text)