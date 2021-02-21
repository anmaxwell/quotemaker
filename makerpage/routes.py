from makerpage import app, db
from makerpage.models import QuoteForm
from makerpage.forms import QuotePage
from flask import render_template, request, redirect, url_for, flash, json
from random import randrange

@app.route("/", methods=['GET','POST'])
def index():

    form = QuoteForm()
    quoteno = randrange(10)
    quotedb = QuoteForm.query.filter(QuoteForm.id == int(quoteno))

    return render_template('index.html', quotedb=quotedb, form=form)