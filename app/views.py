from app import app, db
from app.forms import PersonForm
from app.models import Person
from flask import flash
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.utils import redirect


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PersonForm(request.form, csr_enabled = False)
    people = Person.query.all()

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        contact = request.form.get('contact')
        city = request.form.get('city')
        company = request.form.get('company')

        person = Person(name, email, contact, city, company)
        # saving person to DB
        db.session.add(person)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template('index.html', form=form , people=people)


@app.route("/action/" , methods=['POST'])
def actionOnRecord():
    if request.method == "POST":
        if request.form['submit'] == 'Update':
            # updatation
            person_id = request.form.get('id')
            person_name = request.form.get('name')
            person_email = request.form.get('email')
            person_city = request.form.get("city")
            person_company = request.form.get("company")

            person_to_update = Person.query.filter_by(id=int(person_id))
            person_to_update.name = person_name
            person_to_update.email = person_email
            person_to_update.city = person_city
            person_to_update.company = person_company

            # Saving update
            db.session.commit()
            return redirect(url_for("index"))
        if request.form['submit'] == 'Delete':
            # deletion
            personid = request.form.get('id')
            print( "The Record to be deleted : ", personid)
            if not type(eval(personid)) == int:
                return
            Person.query.filter_by(id=int(personid)).delete()
            db.session.commit() # deletion Completed
            return redirect(url_for("index"))
    return redirect(url_for("index"))