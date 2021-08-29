from converter import convert
from flask import Flask, render_template, request, send_file
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Index.html")

@app.route("/convert")
def convert():
    return render_template("m4atowav.html")

@app.route("/generate", methods=["POST"])
def generate():
    global song
    song = request.form["audio"]
    return render_template("Download.html")


@app.route("/download")
def change():
    convert(song)
    return send_file(path_or_file="Desktop",download_name=song + ".wav", as_attachment=True)


@app.route("/random")
def rand():
    return render_template("HTML.html")


if __name__ == "__main__":
    app.run(debug=True)
