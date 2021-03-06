import numpy as np
import pickle
from flask import Flask, redirect,url_for,render_template, request,jsonify, abort
from flask_bootstrap import Bootstrap
from subprocess import Popen
# 2. Create an app, being sure to pass __name__
app = Flask(__name__, static_folder='./')
Bootstrap(app)
model_open = pickle.load(open('model.pkl','rb'))
 

# 3. Define what to do when a user hits the index route
@app.route('/index.html')
@app.route('/')
def home():
   return app.send_static_file("index.html")

@app.route('/data.html')
def data():
    return app.send_static_file("data.html")

@app.route('/model.html')
def model_player():
    return app.send_static_file("model.html")

@app.route('/model_position.html')
def model_position():
   return app.send_static_file("model_position.html")

@app.route('/player_shots.html')
def player_shots():
   return app.send_static_file("player_shots.html")
 
@app.route('/position_shots.html')
def position_shots():
   return app.send_static_file("position_shots.html")

  
#@app.route('/model_position.html',methods = ['POST'])
##def model():
 ## int_features = [int(x) for x in request.form.values()]
   ## final_features = [np.array(int_features)]
    ##prediction = model.predict(final_features)

    ##output = round(prediction[0],2)
    ##return render_template("model_position.html", prediction_text = 'Shot was made {}').format(output)

@app.route('/predict', methods=['GET','POST'])
def predict():
    data = request.get_json(force=True)
    predict_request = [data['enc_player position'],data['enc_shot outcome']]
    predict_request = np.array(predict_request)
    y_hat = model_open.predict(predict_request)
    output = [y_hat[0]]
    return jsonify(results = output)
 
if __name__ == "__main__":
    app.run(host='localhost', port=5000)
app.run(debug=True)


