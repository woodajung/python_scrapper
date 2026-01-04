# 사전 준비
# pip install beautifulsoup4
# pip install requests

from .utils import get_soup

BASE_URL = "https://berlinstartupjobs.com"

def get_absolute_url(href):
    return href if href.startswith("http") else BASE_URL + href

def parse_jobs(soup):
    jobs = []
    for article in soup.select("li.bjs-jlid"):
        title_tag = article.select_one("h4 a")
        company_tag = article.select_one(".bjs-jlid__company")
        description_tag = article.select_one(".bjs-jlid__description")

        if not title_tag:
            continue

        jobs.append({
            "source": "BerlinStartupJobs",
            "title": title_tag.get_text(strip=True),
            "company": company_tag.get_text(strip=True) if company_tag else "",
            "description": description_tag.get_text(strip=True) if description_tag else "",
            "link": get_absolute_url(title_tag["href"])
        })
    return jobs

def get_total_pages(soup):
    pages = soup.select("a.page-numbers")
    page_numbers = [int(p.text) for p in pages if p.text.isdigit()]
    return max(page_numbers) if page_numbers else 1

def scrape_berlin(skill):
    all_jobs = []

    base_path = f"/skill-areas/{skill}/"
    first_url = BASE_URL + base_path
    soup = get_soup(first_url)
    total_pages = get_total_pages(soup)

    for page in range(1, total_pages + 1):
        if page == 1:
            page_url = first_url
        else:
            page_url = f"{first_url}page/{page}/"

        page_soup = get_soup(page_url)
        all_jobs.extend(parse_jobs(page_soup))

    return all_jobs