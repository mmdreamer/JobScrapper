from flask import Flask, render_template, request, redirect, send_file
from so import get_jobs as so_get_job
from indeed import get_jobs as indeed_get_job
from exporter import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html", bgImage="url('/static/img/bg_home.jpg')")


@app.route("/report")
def report():
    word = request.args.get("word")  # print(request.args.get("word"))
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = so_get_job(word)  # indeed_get_job(word)  +
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultNumber=len(jobs), jobs=jobs, bgImage="none")


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run()
