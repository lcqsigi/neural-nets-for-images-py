# Checkpoint 4: Submitting Data from Web Forms

# web_app/routes/neural_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash # FYI new imports
from werkzeug.utils import secure_filename
import os
os.environ['MKL_THREADING_LAYER'] = 'GNU'

from io import BytesIO
import base64
from PIL import Image

neural_routes = Blueprint("neural_routes", __name__)

# ...

@neural_routes.route("/neural/form")
def neural_form():
    print("NEURAL FORM...")
    return render_template("neural_form.html")

UPLOAD_FOLDER = "."

@neural_routes.route("/neural/prediction", methods=["GET", "POST"])
def neural_prediction():
    print("Neural Network Prediction...")

    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        os.chdir('app')
        os.system('python neural-net.py')

    #if request.method == "GET":
    #    print("URL PARAMS:", dict(request.args))
    #    request_data = dict(request.args)
    #elif request.method == "POST": # the form will send a POST
    #    print("FORM DATA:", dict(request.form))
    #    request_data = dict(request.form)

    #img = BytesIO()

    #plt.savefig(img, format='png')

    #img.seek(0)

    with BytesIO() as output:
        with Image.open('./result.png') as img:
            img.save(output, 'png')
        data = output.getvalue()
    
    plot_url = base64.b64encode(data).decode('utf8')

    os.chdir('..')

    os.system('rm -r app/cats_and_dogs_filtered/ app/result.png file.tar app/file.tar')
                                                        
    return render_template('neural_prediction.html', plot_url=plot_url)
