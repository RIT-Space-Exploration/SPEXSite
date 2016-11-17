from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/hab/')
def hab():
    return render_template('hab.html')


@app.route('/cubesat/')
def cubesat():
    return render_template('cubesat.html')


@app.route('/spexcast/')
def spexcast():
    return render_template('spexcast.html')


@app.route('/sponsors/')
def sponsors():
    return render_template('sponsors.html')

@app.route('/statistics/')
def stats():
    return redirect('http://hab-web-client-hab-telemetry-server.app.csh.rit.edu/statistics')

@app.route('/orientation/')
def orientation():
    return redirect('http://hab-web-client-hab-telemetry-server.app.csh.rit.edu/orientation')
