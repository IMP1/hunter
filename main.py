# pip install beautifulsoup4 (https://pypi.org/project/beautifulsoup4/)
import plac
from job_site_parser import *


URL_SCRAPERS = {
    # URL: (ParserClass, HTTP_POST_Settings)
    "https://stackoverflow.com/jobs": (StackOverflowJobParser, None),
    "https://www.linkedin.com/jobs/": (LinkedInJobParser, None),
    "https://doinggoodleeds.org.uk/jobs/": (DoingGoodLeedsJobParser, None),
    "https://www.indeed.co.uk/jobs?q=&l=Leeds": (IndeedJobParser, None),
}


last_fetch = None


def pages():
    import urllib2
    pages = []
    for url in URLS:        
        response = urllib2.urlopen(url)
        html = response.read()
        pages.append(html)
    return pages


def parse_html(pages):
    from bs4 import BeautifulSoup 
    parsed_pages = []
    for page in pages:
        html_object = BeautifulSoup(page)
        parsed_pages.append(html_object)
    return parsed_pages


def parse_jobs(pages):
    jobs = []
    for page in pages:
        jobs.extend(JobSiteParser.parse(html))
    return jobs


def fetch_jobs():
    print("Fetching jobs... ", end='')
    from datetime import datetime
    page_texts = get_pages()
    html_objects = parse_html()
    jobs = parse_jobs()
    # Output jobs somewhere
    last_fetch = datetime.utcnow()
    print("Done. ")


def search_jobs():
    print("Searching jobs... ", end='')
    print("Done. ")


@plac.annotations(
    command=("The path to documents to search", "positional", None, str, ["fetch", "search"]),
)
def main(command):
    if command == "fetch":
        fetch_jobs()
    elif command == "search":
        search_jobs()


if __name__ == "__main__":
    plac.call(main)
