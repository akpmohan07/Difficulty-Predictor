from flask import Flask ,render_template,request 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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
    data = data.drop('Attended',axis=1)
    dummy = pd.get_dummies(data.Question_Type)
    data = pd.concat([data,dummy],axis='columns')
    data = data.drop('Question_Type',axis = 'columns')
    le = LabelEncoder()
    data.Question_Difficulty = le.fit_transform(data.Question_Difficulty)
    x = data.drop('Question_Difficulty',axis = 1)
    y = data['Question_Difficulty']
    train,test,train_label,test_label = train_test_split(x,y,random_state = 0)
    dtc = DecisionTreeClassifier(max_depth=2)
    dtc.fit(train,train_label)
    score = dtc.score(test,test_label)
    return render_template('predict.html',url = score)
    

if __name__ == "__main__":
    app.run(debug=True)