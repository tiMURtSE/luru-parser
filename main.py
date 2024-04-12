import fnmatch
from collections import deque
from basic_decor_library.Browser import Browser
from models.SessionData.SessionData import SessionData
from models.SessionDataHandler.SessionDataHandler import SessionDataHandler
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from consts import START_URL, DISALLOWED_PATHS

class Main:
    def __init__(self):
        # self._browser = Browser()
        self._session_data = SessionDataHandler()

    def run(self):
        json_data = self._session_data.read_data()
        link_queue = deque([START_URL, *json_data["queue"]])
        visited_pages = set([START_URL, *json_data["visited"]])

        data = SessionData(queue=link_queue, visited=visited_pages)
        self._session_data.write_data(data=data)

        # while link_queue:
        #     current_link = link_queue.popleft()


























































    def _robot_txt_check(self, url: set):
        for disallow in DISALLOWED_PATHS:
            if fnmatch.fnmatch(url, disallow):
                print(f"pizdec dlya {url}")
                return True

app = Main()
app.run()



def meow():
    start_url = "https://lu.ru"
    queue = deque([start_url])
    visited = set()
    visited.add(start_url)

    while queue:
        current_url = queue.popleft()

        try:
            self._browser.get(url=current_url)
            # if self._robot_txt_check(url=current_url):
            #     continue

            print("Current url:", current_url)
            # Do something...

            link_elements = self._browser._wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a")))
            links = set([element.get_attribute("href") for element in link_elements])

            for link in links:
                if link not in visited:
                    queue.append(link)
                    visited.add(link)
        except Exception as e:
            print(e)
            continue