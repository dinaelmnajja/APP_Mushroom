from flask import Flask, render_template, request
import pickle

app = Flask(__name__,static_url_path='/static')
model = pickle.load(open('C:/Users/VIET/Desktop/APP_Mushroom/model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict',methods=['POST'])

def predict():

    error_message = None 

    if request.method == 'POST':

         bruises = float(request.form['bruises'])
         gill_spacing = float(request.form['gill_spacing'])
         gill_size = float(request.form['gill_size'])
         gill_color = float(request.form['gill_color'])
         ring_type = float(request.form['ring_type'])
         result = model.predict([[bruises, gill_spacing, gill_size, gill_color,ring_type]])[0]

         

    if not (bruises and gill_spacing and gill_size and gill_color and ring_type):
            error_message = "Please fill in all required fields."
            return render_template('index.html', error_message=error_message)
  


    if result == 1:
        Class ="The Mushroom is edible"

    if result == 2:
        Class = "The Mushroom is toxic"
        

    return render_template('index.html', result=Class)




if __name__ == "__main__":
    app.run(debug=True)