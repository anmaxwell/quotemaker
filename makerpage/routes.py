from makerpage import app, db
from makerpage.models import QuoteForm
from makerpage.forms import QuotePage
from flask import render_template, request, redirect, url_for, flash, json

@app.route("/", methods=['GET', 'POST'])
def index():

    form = QuoteForm()

    return render_template('quotepage.html', form=form)