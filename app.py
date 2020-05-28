from flask import Flask ,render_template,request 
import pickle
import pandas as pd
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    url = request.form['url']
    data = pd.read_csv(url)
    return render_template('predict.html',url = data.to_html())
    

if __name__ == "__main__":
    app.run(debug=True)