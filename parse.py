from clarifai import rest

from clarifai.rest import ClarifaiApp

app = ClarifaiApp("mX0pu-yOLsBVMbVEp5cP-I74em1-AnxQug4h1iLB", "HdMrFacv2Y9b54jjbS9k3jd70kqtZ72kPihB0TqW")

model = app.models.get("general-v1.3")



image = 'https://www.royalcanin.com/~/media/Royal-Canin/Product-Categories/cat-adult-landing-hero.ashx'



def parse(image):
    output = str(model.predict_by_url(url=image))
    index = output.find("u'name'") + 1
    concepts = []
    for i in range(1, output.count("u'name'")):
        index = output.find("u'name'", index + 1)
        concepts.append(output[index + 11:output.find("'", index + 13)])
    return concepts

print(parse(image))


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/send', methods=['POST'])
def send():
    response = parse(request.form["url"])
    return str(response)
    

app.run(debug=True)