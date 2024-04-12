from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from basic_decor_library.Browser import Browser

class AllCategoriesPage(Browser):
    CATEGORY_LINK = "lighting-block-link"

    def __init__(self):
        super().__init__()

    def get_category_links(self):
        """
        Получает ссылки всех категорий.
        """
        category_elements = self._wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, self.CATEGORY_LINK)))
        category_links = [element.get_attribute("href") for element in category_elements]

        return category_links