class Job:

    def __init__(self, title, description, salary, hours, url):
        self.title = title
        self.description = description
        self.salary = salary
        self.hours = hours
        self.url = url


class JobSiteParser:

    @staticmethod
    def parse(html):
        # Determine which parser to use based off some identifiying feature from the HTML
        # Create an instance of the appropriate class
        # Run parse on that class
        # Return the jobs
        pass


class StackOverflowJobParser(JobSiteParser):
    pass


class LinkedInJobParser(JobSiteParser):
    pass


class DoingGoodLeedsJobParser(JobSiteParser):
    pass


class IndeedJobParser(JobSiteParser):
    pass

