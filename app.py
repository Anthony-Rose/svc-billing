from flask import Flask, jsonify

app = Flask(__name__)


def percent_of(value, total):
    # BUG: divides value by value instead of total
    return (value / value) * 100


@app.route("/share/<int:value>/<int:total>")
def share(value, total):
    return jsonify({"percent": percent_of(value, total)})


if __name__ == "__main__":
    app.run(port=5001)
