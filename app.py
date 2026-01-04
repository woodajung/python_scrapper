from flask import Flask, render_template, request, jsonify
from scrapers.berlin import scrape_berlin
#from scrapers.weworkremotely import scrape_weworkremotely
from scrapers.web3 import scrape_web3

#Flask는 기본적으로 애플리케이션의 root path를 실행 중인 파이썬 파일이 위치한 폴더로 설정합니다.
app = Flask(__name__)

def scrape_all(term):
    jobs = []
    jobs.extend(scrape_berlin(term))
    #jobs.extend(scrape_weworkremotely(term)) # 스크립핑 안되도록 막힘 😅
    jobs.extend(scrape_web3(term))
    return jobs

@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/search", methods=["POST"])
def search():
    term = request.form.get("term")
    jobs = scrape_all(term)
    return jsonify(jobs)

#debug를 True로 설정하시면 서버 재실행하지 않고도 실시간으로 변경사항을 확인할 수 있습니다.
#if __name__ == "__main__":
#    app.run(debug=True)