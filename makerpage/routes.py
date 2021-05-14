from makerpage import app, db
from makerpage.models import QuoteForm
from makerpage.forms import QuotePage
from flask import render_template, request, redirect, url_for, flash, json
from random import randrange
import gpt_2_simple as gpt2
import requests

@app.route("/", methods=['GET','POST'])
def index():

    form = QuoteForm()

    #to test using quotes from a database
    #quoteno = randrange(1,10)
    #quotedb = QuoteForm.query.filter(QuoteForm.id == int(quoteno))

    #to load model and create quotes
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    text = gpt2.generate(sess,
              length=100,
              temperature=0.7,
              truncate='.',
              nsamples=1,
              return_as_list=True
              )[0]

    #to randomly choose between the backgrounds
    image = randrange(1,13) 
    background = "%s%s" % (image, ".jpg")

    return render_template('index.html', form=form, background=background, text=text)

@app.route("/send/<string:text>", methods=['GET','POST'])
def send(text):

    scheme = 'http'
    uri = 'host.docker.internal'
    port = 5000

    url = f'{scheme}://{uri}:{port}/api/addquote'

    data = {'quote':text}

    r = requests.post(url = url, json = data)

    return redirect(url_for('index')) 