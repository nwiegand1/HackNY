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


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('main.html')

@app.route('/link/')
	print(parse(form.url))









  import web

  urls = ('/send', 'Index')

	app = web.application(urls, globals())

	render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.main()

    def POST(self):
        form = web.input(url="https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/30423_pets-products_january-site-flip_3-cathealth_short-tile_592x304._CB286975940_.jpg")
        keywords = parse(form.url)
        return render.index(keywords = keywords)

if __name__ == "__main__":
    app.run()
