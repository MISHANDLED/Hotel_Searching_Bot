from selenium.webdriver.remote.webdriver import WebDriver


class BookFilter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star(self, *star_values):
        star_filter = self.driver.find_element_by_id('filter_class')
        star_filter_child = star_filter.find_elements_by_css_selector('*')

        for star_value in star_values:
            for ele in star_filter_child:
                if str(ele.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    ele.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        element.click()

