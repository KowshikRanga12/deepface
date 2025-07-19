from flask import Flask,redirect,url_for,render_template,request
from deepface import DeepFace
import os

UPLOAD_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/compare',methods=['GET','POST'])
def compare(): 
    if request.method == 'POST':
        image1 = request.files['image1']
        image2 = request.files['image2']
        if image1 and image2:
            image1_path = f'static/{image1.filename}'
            image2_path = f'static/{image2.filename}'
            image1.save(image1_path)
            image2.save(image2_path)
            
            result = DeepFace.verify(image1_path, image2_path)
            if result['verified']:
                message = "The images are of the same person."
            else:
                message = "The images are of different people."
            
            return render_template('compare.html', message=message)
        return redirect(url_for('home'))
    
    return render_template('compare.html')
if __name__ == '__main__':
    app.run(debug=True)