import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, send_from_directory, current_app
import subprocess as sp
FFMPEG = "C:\\ffmpeg\\bin\\ffmpeg.exe"
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Index.html")


@app.route("/convert")
def audio():
    return render_template("m4atowav.html")


@app.route("/m4atowav", methods=["POST"])
def generate():
    global dfile
    file = request.files['audio']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.instance_path, 'uploads', filename))
    dfile = '{}.{}'.format(os.path.splitext(filename)[0], ".wav")
    inp = os.path.join(app.instance_path, 'uploads', filename)
    out = os.path.join(app.instance_path, 'downloads', dfile)
    convertcmd = [FFMPEG, '-i', inp, '-y', out]
    downl = sp.Popen(convertcmd,shell=True)
    try:
        outs, errs = downl.communicate(timeout=10)
    except TimeoutError_:
        proc.kill()
    return render_template("Download.html")



@app.route("/download")
def change():
    ddir = os.path.join(current_app.root_path, app.instance_path, 'downloads')
    return send_from_directory(directory=ddir, path="instance\\downloads", filename=dfile, as_attachment=True)


@app.route("/random")
def rand():
    return render_template("HTML.html")


if __name__ == "__main__":
    app.run(debug=True)
