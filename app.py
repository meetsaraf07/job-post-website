from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': "New York",
    'salary': '$100000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': "San Francisco",
    'salary': '$120000'
}, {
    'id': 3,
    'title': 'Data Engineer',
    'location': "remote",
}, {
    'id': 4,
    'title': 'Data Architect',
    'location': "New York",
    'salary': '$150000'
}]


@app.route("/")
def home_page():
    return render_template(
        "home.html",
        jobs=jobs,#pass the jobs list to the template
        company_name="__"#add your company name here
    )

@app.route("/api/jobs_list")
def jobs_list():
    return jsonify(jobs)

if (__name__ == "__main__"):
    app.run(debug=True, host="0.0.0.0", port=8000)
