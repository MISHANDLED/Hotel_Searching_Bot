from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, parent_element: WebElement):
        self.parent_element = parent_element
        self.hotel_lists = self.pull_hotels()

    def pull_hotels(self):
        return self.parent_element.find_elements_by_class_name('sr_property_block')

    def pull_hotel(self):
        list_hotel = []

        for name in self.hotel_lists:
            hotel_name = name.find_element_by_class_name('sr-hotel__name').get_attribute('innerHTML').strip()
            hotel_price = name.find_element_by_class_name('bui-price-display__value').get_attribute('innerHTML').strip()
            hotel_score = name.get_attribute('data-score').strip()

            list_hotel.append(
                [hotel_name, hotel_price, hotel_score]
            )

        return list_hotel
