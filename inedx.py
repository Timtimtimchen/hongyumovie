from flask import Flask,render_template,redirect
import requests,bs4

app = Flask(__name__)
@app.route("/")
def inin():
    return render_template("index.html")

@app.route("/movie")
def index():
    a = requests.get("http://www.atmovies.com.tw/movie/next/",headers={"User-Agent":
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
    a.encoding= "utf-8"
    text = bs4.BeautifulSoup(a.text,"html.parser")
    time = text.find("div",class_="smaller09 grey center")
    return time.text.replace("更新時間：","近期上映電影已爬蟲及存檔完畢，網站最近更新日期為：")
