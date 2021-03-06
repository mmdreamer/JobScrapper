import requests
from bs4 import BeautifulSoup


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("ul", {"class": "pagination-list"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"].strip("-")
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company:
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None

    location = html.find("span", {"class", "location"}).string
    job_id = html["data-jk"]
    return {"title": title, "company": company, "location": location, "apply_link": f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed : Page {page}")
        result = requests.get(f"{url}&start={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all(
            "div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = "https://www.indeed.com/jobs?q={word}}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
