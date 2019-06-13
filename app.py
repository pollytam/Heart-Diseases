# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
from sklearn.externals import joblib

app = Flask(__name__)

# Load the model
# model = pickle.load(open('./model/QDA_model.pkl','rb'))

# <a action="/action_page.php" target="_parent" a/>

# with action tag, when action is executed, you can target the bottom of the page as output


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/quiz/')
def quiz():
    return render_template("quiz.html")

@app.route('/tableau/')
def tableau():
    return render_template('tableau.html')

@app.route('/graph1/')
def graph1():
    return render_template('graph1.html')

@app.route('/graph2/')
def graph2():
    return render_template('graph2.html')

@app.route('/predict',methods=['POST'])

def predict():
    # Get the data from the POST request.
    if request.method == "POST":
            # Load the model
        model = pickle.load(open('./model/rf_model1.pkl','rb'))
        ## ["1, 3,34, 5"]  => ["1", "2", "3", "4"]
        ## [1.0 3.0, 4.0, 4.0, 5.0]
        #data = request.get_json(force=True)
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        a = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        print(a)
        a = [float(b) for b in a]
        print(a)
        # print(request.form['exp'])
        # data = float(request.form['exp'])
        print("Data", model.predict([a]))
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([a])

        # Take the first value of prediction
        output = prediction[0]
        if output == 0:
            output = "Negative! Yay! The model believes that you don't have the heart diseases."
            
        else:
            output = "Positive! Oh! The model believes that you are likely to have the heart diseases."
           

        return render_template("quiz.html", output=output, exp=a)

if __name__ == '__main__':
    app.run(debug=True)
