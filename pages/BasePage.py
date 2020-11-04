import urllib.parse


class Page(object):
    BASE_URL = 'https://id.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self, url=None):
        if (url == None):
            url = self.BASE_URL
        url = urllib.parse.urljoin(url, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
