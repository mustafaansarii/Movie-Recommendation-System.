from flask import Flask, render_template, request
import modelbit
import pandas as pd

app = Flask(__name__)

def recommend(movie_name):
    response_json = modelbit.get_inference(
        region="ap-south-1",
        workspace="mustafaansari",
        deployment="recommend",
        data=movie_name
    )
    data_list = response_json['data']
    df = pd.DataFrame(data_list)
    # Reset index to start from 1 instead of 0
    df.index = df.index + 1
    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        df = recommend(movie_name)
        return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
