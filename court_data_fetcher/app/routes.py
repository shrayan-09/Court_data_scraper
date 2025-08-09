from flask import render_template, request, redirect, flash
from . import db
from .models import QueryLog
from .scraper import fetch_case_details_delhi
from flask import current_app as app

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        try:
            raw_html, parsed = fetch_case_details_delhi(case_type, case_number, filing_year)

            log = QueryLog(
                case_type=case_type,
                case_number=case_number,
                filing_year=filing_year,
                raw_html=raw_html,
                parsed_data=parsed
            )
            db.session.add(log)
            db.session.commit()

            return render_template('form.html', data=parsed)

        except Exception as e:
            flash(str(e), 'danger')

    return render_template('form.html')
