from .utils import get_soup

BASE_URL = "https://web3.career"

HEADERS = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_web3(skill):
    url = f"{BASE_URL}/{skill}-jobs"
    soup = get_soup(url)

    jobs = []
    for job in soup.select("tr.table_row"):
        title = job.select_one("h2")
        company = job.select_one("h3 a")

        if not title:
            continue

        jobs.append({
            "source": "Web3.career",
            "title": title.get_text(strip=True),
            "company": company.get_text(strip=True) if company else "",
            "description": "",
            "link": BASE_URL + company["href"] if company else ""
        })
    return jobs
