from makerpage import app, db
from makerpage.models import QuoteForm
from makerpage.forms import QuotePage
from flask import render_template, request, redirect, url_for, flash, json
from random import randrange

@app.route("/", methods=['GET','POST'])
def index():

    form = QuoteForm()

    #to test using quotes from a database
    quoteno = randrange(1,10)
    quotedb = QuoteForm.query.filter(QuoteForm.id == int(quoteno))

    #to randomly choose between the backgrounds
    image = randrange(1,13) 
    background = "%s%s" % (image, ".png")

    return render_template('index.html', quotedb=quotedb, form=form, background=background)