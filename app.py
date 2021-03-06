from flask import Flask ,render_template,request,send_from_directory
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
import pandas as pd
app = Flask(__name__)
model = pickle.load(open('dtc_model.pkl', 'rb')) #Loading the Model from pickle file
@app.route('/') #Home Page
def home():
    return render_template('index.html')
@app.route('/about')
def about(): #About
    return render_template('simple_about.html')
@app.route('/predict',methods=['GET','POST']) #Predict
def predict():

    if request.form['action'] == 'file':# File as input
        url = request.form['url'] #Getting URL
        data = pd.read_csv(url) #Loading data from URL
        backup = data
        data = data.drop('Attended',axis=1) 
        dummy = pd.get_dummies(data.Question_Type) #Handling Categorical Data
        data = pd.concat([data,dummy],axis='columns')
        data = data.drop('Question_Type',axis = 'columns')
        le = LabelEncoder() 
        label = le.fit_transform(['Easy','Medium','Hard'])
        try:#If the  file had target attribute it is dropped
            x = data.drop('Question_Difficulty',axis = 1)
        except:
            x = data

        #y = data['Question_Difficulty']
        #train,test,train_label,test_label = train_test_split(x,y,random_state = 0)
        # dtc = DecisionTreeClassifier(max_depth=2)
        # dtc.fit(train,train_label)
        # score = dtc.score(test,test_label)
        #print(x)
        #score = model.score(x,y)
        pre = model.predict(x) #Predicting
        pr = list(le.inverse_transform(pre)) #inverse Labelling
        backup['Predicted'] = pr
        return render_template('predict.html',url = url,tables=[backup.to_html(classes='data')],titles=backup.columns.values)
    elif request.form['action'] == 'form': #If Feature as input
        data = []
        data.append(request.form['QT']) #Getting form data
        data.append(request.form['TT'])
        data.append(request.form['S'])
        data.append(request.form['HU'])
        data.append(request.form['R'])
        data.append(request.form['P'])
        data.append(request.form['W'])
        if data[0] == 'MCQ':    #Handing Categorical data
            data.extend([0,1,0,0])
        elif data[0] == 'FillUp':
            data.extend([1,0,0,0])
        elif data[0] == 'Match':
            data.extend([0,0,1,0])
        else:
            data.extend([0,0,0,1])
        del data[0]
        data = list(map(int,data))
        print(data)
        pred = model.predict([data]) #predicting
        if pred==0: #Reverse Labelling
            diff = "Easy"
        elif pred==1:
            diff = "Hard"
        else:
            diff = "Medium"
        return render_template('predict.html',level=diff)


if __name__ == "__main__":
    app.run(debug=True)