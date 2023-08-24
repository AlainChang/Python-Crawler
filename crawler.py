from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import matplotlib.pyplot as plt
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/titlepage")
def page():
    options = Options()
    options.chrome_executable_path = (
        "C:\\Users\alen7\Desktop\Homework\crawlerproject\chromedriver.exe"
    )

    driver = webdriver.Chrome(options=options)
    driver.get(
        "https://www.linkedin.com/jobs/search?keywords=&location=%E5%8F%B0%E7%81%A3&geoId=104187078&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    )

    n = 0
    while n < 10:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        n += 1

    titleTags = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
    locations = driver.find_elements(
        By.CLASS_NAME,
        "job-search-card__location",
    )
    subtitles = driver.find_elements(By.CLASS_NAME, "base-search-card__subtitle")

    tit = []
    subtit = []
    locals = []

    for titleTag in titleTags:
        tit.append(titleTag.text)
        print(titleTag.text)

    titlen = len(tit)
    print(titlen)

    for subtitle in subtitles:
        subtit.append(subtitle.text)
        print(subtitle.text)

    for location in locations:
        locals.append(location.text)
        print(location.text)

    driver.close()

    return render_template(
        "crawler.html", titlet=tit, local=locals, subt=subtit, titlen=titlen
    )


@app.route("/localdash")
def dash():
    options = Options()
    options.chrome_executable_path = (
        "C:\\Users\alen7\Desktop\Homework\crawlerproject\chromedriver.exe"
    )

    driver = webdriver.Chrome(options=options)
    driver.get(
        "https://www.linkedin.com/jobs/search?keywords=&location=%E5%8F%B0%E7%81%A3&geoId=104187078&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    )

    n = 0
    while n < 10:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        n += 1

    titleTags = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
    locations = driver.find_elements(
        By.CLASS_NAME,
        "job-search-card__location",
    )

    tit = []
    locals = []

    for titleTag in titleTags:
        tit.append(titleTag.text)

    for location in locations:
        locals.append(location.text)

    driver.close()

    plt.figure(figsize=(50, 50), dpi=100)
    plt.scatter(tit, locals)
    plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
    plt.show()
    return redirect("/")


@app.route("/companydash")
def cls():
    options = Options()
    options.chrome_executable_path = (
        "C:\\Users\alen7\Desktop\Homework\crawlerproject\chromedriver.exe"
    )

    driver = webdriver.Chrome(options=options)
    driver.get(
        "https://www.linkedin.com/jobs/search?keywords=&location=%E5%8F%B0%E7%81%A3&geoId=104187078&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    )

    n = 0
    while n < 10:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        n += 1

    titleTags = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
    subtitles = driver.find_elements(By.CLASS_NAME, "base-search-card__subtitle")

    tit = []
    subtit = []

    for titleTag in titleTags:
        tit.append(titleTag.text)
        print(titleTag.text)

    for subtitle in subtitles:
        subtit.append(subtitle.text)
        print(subtitle.text)

    driver.close()

    plt.figure(figsize=(100, 100), dpi=100)
    plt.scatter(tit, subtit)
    plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
    plt.show()

    return redirect("/")


if __name__ == "__main__":
    app.run()
