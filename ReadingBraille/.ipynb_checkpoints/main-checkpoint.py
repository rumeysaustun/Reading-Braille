from flask import Flask, request, render_template
from flask import Flask, url_for, render_template,request, send_from_directory,redirect,flash,json,send_file
import cv2
import numpy as np
from random import randint
import os
import shutil
import tespit

app = Flask(__name__)
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def detect_objects(image):

    return [("araba", 100, 200, 300, 400), ("köpek", 50, 100, 150, 200)]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image'].read()

        npimg = np.fromstring(image, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        objects = detect_objects(img)

        return render_template('result.html', objects=objects)

    return render_template('index-yeni.html')

@app.route('/dosya-ekle', methods=['POST'])
def dosyaEkle():
    file = request.files['image']    
    filename = 'Images-' + str(randint(0,99999999)) + '-no.jpg'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    tespit.tespitEt(filename)
    img_path=  "../runs/detect/exp/" + filename
    print(img_path)
    return render_template('result.html',img_path=img_path)



if __name__ == '__main__':
    app.run(debug=True)


