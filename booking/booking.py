from selenium import webdriver
from booking.book_filter import BookFilter
from booking.report import BookingReport
from prettytable import PrettyTable
import os
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()

        selected_element_curr = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="changed_currency=1;selected_currency={currency};top_currency=1"]'
        )
        selected_element_curr.click()

    def textfield_filler(self, name='Delhi'):
        location = self.find_element_by_id('ss')
        location.clear()
        location.send_keys(name)
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

    def date_select(self, start_date, end_date):
        day1 = self.find_element_by_css_selector(
            f'td[data-date="{start_date}"]'
        )
        day1.click()

        dayn = self.find_element_by_css_selector(
            f'td[data-date="{end_date}"]'
        )
        dayn.click()

    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()

            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute(
                'value'
            )

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count - 1):
            increase_button_element.click()

    def select_rooms(self, count=1):
        select_ele = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Rooms"]'
        )

        for _ in range(count - 1):
            select_ele.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filter(self):
        filtration = BookFilter(driver=self)
        filtration.apply_star(3, 4, 5)
        filtration.sort_price_lowest_first()

    def hotel_results(self):
        hotel_list = self.find_element_by_id('hotellist_inner')
        report = BookingReport(hotel_list)
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_hotel())
        print(table)

