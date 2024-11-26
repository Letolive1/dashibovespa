from flask import Flask, jsonify, render_template, send_file
import os
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    df = pd.read_csv('data/stock_data.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/plots/<plot_name>')
def plots(plot_name):
    plot_path = f'static/{plot_name}.png'
    if os.path.exists(plot_path):
        return send_file(plot_path, mimetype='image/png')
    return "Plot not found", 404

if __name__ == '__main__':
    app.run(debug=True)