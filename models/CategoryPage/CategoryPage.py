from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from basic_decor_library.Browser import Browser
from models.Category.Category import Category

class CategoryPage(Browser):
    HEADER_CLASS = "h1-page"
    KEYWORDS_SELECTOR = "meta[name='keywords']"
    DESCRIPTION_SELECTOR = "meta[name='description']"
    OG_TITLE_SELECTOR = "meta[property='og:title']"
    OG_URL_SELECTOR = "meta[property='og:url']"

    def __init__(self):
        super().__init__()

    def get_categories(self, category_links: list[str]):
        categories = []

        for link in category_links:
            self._browser.get(url=link)
            category = self._get_category()
            categories.append(category)

        return categories

    def _get_category(self):
        header = self._get_category_header()
        keywords = self._get_keywords()
        description = self._get_description()
        og_title = self._get_og_title()
        og_url = self._get_og_url()

        category = Category(
            header=header,
            keywords=keywords,
            description=description,
            og_title=og_title,
            og_url=og_url
        )

        return category

    def _get_category_header(self):
        header_element = self._wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.HEADER_CLASS)))
        header = header_element.text

        return header
    
    def _get_keywords(self):
        keywords_element = self._browser.find_element(By.CSS_SELECTOR, self.KEYWORDS_SELECTOR)
        keywords = keywords_element.get_attribute("content")

        return keywords
    
    def _get_description(self):
        description_element = self._browser.find_element(By.CSS_SELECTOR, self.DESCRIPTION_SELECTOR)
        description = description_element.get_attribute("content")

        return description
    
    def _get_og_title(self):
        og_title_element = self._browser.find_element(By.CSS_SELECTOR, self.OG_TITLE_SELECTOR)
        og_title = og_title_element.get_attribute("content")

        return og_title
    
    def _get_og_url(self):
        og_url_element = self._browser.find_element(By.CSS_SELECTOR, self.OG_URL_SELECTOR)
        og_url = og_url_element.get_attribute("content")

        return og_url