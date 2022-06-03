import os
import datetime
from werkzeug.utils import secure_filename

from flask import Flask, redirect, render_template, request, send_from_directory
import cv2


upload_file="static/uploads/"

app = Flask(__name__)
app.config['upload_file'] = upload_file

@app.route('/', methods=['GET', 'POST'])
def index():
    images = os.listdir(upload_file)
    if request.method == 'GET':
        return render_template('index.html', title='Anasayfa', uploads=images)
        
    if request.method == 'POST':
        target = os.path.join(upload_file)

        file = request.files['file']
        filename = secure_filename(file.filename)
        new_name = datetime.datetime.now().strftime("%d%b%y-%f") + '.' + filename.split('.')[1]
        new_file = '/'.join([target, new_name])

        file.save(new_file)



        image = cv2.imread('./static/uploads/'+new_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(gray,(3,3),0)
        laplacian = cv2.Laplacian(img,cv2.CV_64F)
        sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
        cv2.imwrite('./static/laplacian/'+new_name, laplacian)
        cv2.imwrite('./static/sobelx/'+new_name, sobelx)
        cv2.imwrite('./static/sobely/'+new_name, sobely)

        return redirect('/')

@app.route('/galeri')
def galeri():
    images = os.listdir(upload_file)
    return render_template('galeri.html', title='Galeri', uploads=images)

@app.route('/galeri/<filename>')
def upload(filename):
    return render_template('detail.html', title=filename, image=filename)

app.run(debug=True)