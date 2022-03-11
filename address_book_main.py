from address_book_console import AddressBookConsoleService

if __name__ == "__main__":

    print("Welcome to Address Book Management System")
    console_service = AddressBookConsoleService()

    while True:
        print(" 1 Add Contact "
              "\n 2 Display Contact"
              "\n 3 Edit Contact"
              "\n 4 Delete Contact"
              "\n 5 Search by City or State"
              "\n 6 View Person by City or State"
              "\n 0 Exit")

        input_dict = {
            1: console_service.add_contact,
            2: console_service.display_contact,
            3: console_service.edit_contact,
            4: console_service.delete_contact,
            5: console_service.search_person_by_location,
            6: console_service.view_person_by_location,
            7: exit
        }
        user_choice = int(input())
        input_dict[user_choice]()
