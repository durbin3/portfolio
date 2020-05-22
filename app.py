from flask import Flask, render_template, send_file
app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


@app.route("/challenges")
def challenges():
    return render_template('challenges.html')


@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/resume")
def download_resume():
    return send_file("static/files/resume.pdf")

if __name__ == '__main__':
    app.run(debug = True)
