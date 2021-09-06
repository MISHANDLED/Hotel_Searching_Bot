from booking.booking import Booking


try:
    location = input("Destination: ")
    start_date = input("Enter From Date (in YYYY-MM-DD): ")
    end_date = input("Enter To Date (in YYYY-MM-DD): ")
    adults = int(input("Number of Adults: "))
    rooms = int(input("Number of Rooms Required: "))

    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.textfield_filler(location)
        bot.date_select(start_date=start_date, end_date=end_date)
        bot.select_adults(adults)
        bot.select_rooms(rooms)
        bot.click_search()
        bot.apply_filter()
        bot.refresh()
        bot.hotel_results()
        bot.close()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
