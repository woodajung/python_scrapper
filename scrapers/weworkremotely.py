from .utils import get_soup

BASE_URL = "https://weworkremotely.com"

def scrape_weworkremotely(skill):
    url = f"{BASE_URL}/remote-jobs/search?term={skill}"
    soup = get_soup(url)

    jobs = []
    for section in soup.select("section.jobs"):
        for job in section.select("li > a"):
            title = job.select_one("span.title")
            company = job.select_one("span.company")

            if not title:
                continue

            jobs.append({
                "source": "WeWorkRemotely",
                "title": title.get_text(strip=True),
                "company": company.get_text(strip=True) if company else "",
                "description": "",
                "link": BASE_URL + job["href"]
            })
    return jobs
