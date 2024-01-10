from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import joblib
from flask import flash


app = Flask(__name__)

# Replace these paths with the actual paths of your model and vectorizer files
model_path = 'C:\\Users\\svani\\OneDrive\\Documentos\\DineshKumar\\Project\\Sentiment Analysis Website\\Model\\Sentiment_classifier_model.joblib'
vectorizer_path = 'C:\\Users\\svani\\OneDrive\\Documentos\\DineshKumar\\Project\\Sentiment Analysis Website\\Model\\vectorizer_model.joblib'

# Load your sentiment analysis model and vectorizer

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/SENTIMENT_ANALYSIS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for internship registration
class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), nullable=False)
    Phone_Number = db.Column(db.String(15), unique=True, nullable=False)
    New_Password = db.Column(db.String(15), unique=True, nullable=False)
    Confirm_Password = db.Column(db.String(15), unique=True, nullable=False)

# Route for internship registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['name']
        email_id = request.form['email']
        phone_number = request.form['phone']
        New_Password = request.form['newPassword']
        Confirm_Password = request.form['confirmPassword']
        connection = db.engine.connect()
        
        registration =users(
                Name=  full_name,
                Email= email_id,
                Phone_Number=  phone_number,
                New_Password= New_Password,
                Confirm_Password = Confirm_Password 
        )

        db.session.add(registration )
        db.session.commit()# Close the database connection

     
        return redirect(url_for('registration_success'))

    return render_template('Registration_page.html')

# Route for displaying registration success
@app.route('/success')
def registration_success():
    return render_template('registration_success.html')


# Placeholder for the sentiment analysis function
def predict_sentiment(text):
        # Transform the text using the loaded vectorizer
        text_vectorized = vectorizer.transform([text])

        # Make predictions using the loaded model
        prediction = model.predict(text_vectorized)[0]

        return prediction
    
# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('Loginpage.html')

# Route for the sentiment analysis form
@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    if request.method == 'POST':
        user_input = request.form['text']
        prediction = predict_sentiment(user_input)
        return render_template('Result.html', user_input=user_input, prediction=prediction)

    return render_template('Sentiment-Analysis.html')

# Route for displaying sentiment analysis results
@app.route('/result', methods=['GET', 'POST'])
def result():
    user_input = request.args.get('text')
    prediction = request.args.get('prediction')

    if user_input is not None and prediction is not None:
        return render_template('Result.html', user_input=user_input, prediction=prediction)
    else:
        return render_template('Result.html', user_input="", prediction="")

if __name__== '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

