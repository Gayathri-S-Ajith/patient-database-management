# app.py
from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate(r"C:\Users\HP\OneDrive\Desktop\flask\hacksthon-dca7a-firebase-adminsdk-bxiir-ac9a95ff57.json")  # Update path
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    patient_name = request.form['patientName']
    appointment_date = request.form['appointmentDate']
    # Save data to Firebase
    doc_ref = db.collection('appointments').add({
        'patientName': patient_name,
        'appointmentDate': appointment_date
    })
    return 'Appointment booked successfully!'


@app.route('/doctor', methods=["GET", "POST"])
def doctor():
    
    return render_template('doctor.html')  # Example rendering of doctor form template




if __name__ == '__main__':
    app.run(debug=True)
