from address_book_console import AddressBookConsoleService

if __name__ == "__main__":
    console_service = AddressBookConsoleService()
    print("Welcome to Address Book Management System")
    contact = console_service.create_contact()
    console_service.display_contact(contact)