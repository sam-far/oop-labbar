import datetime

class Person():
    def __init__(self, birthdate):
        """
        Alla har ett födelsedatum
        """
        self.birthdate = birthdate
    
    def add_name(self, name):
        """
        Lägg till ett namn på Person
        """
        self.name = name

    def change_address(self, address, zipcode, city):
        """
        Lägga till och ändra adress
        """
        self.address = address
        self.zipcode = zipcode
        self.city = city

    def current_age(self):
        """
        Beräkna ålder
        """
        return datetime.date.today().year - self.birthdate
        

if __name__ == "__main__":

    # Födda
    sam        = Person(1980)
    sam_age    = Person(1980).current_age()
    sexig_brud = Person(1995)
    sexig_age  = Person(1995).current_age()

    # Namn
    sam.name = "Sam Ashkan Far"
    sexig_brud.name = "Kate Upton"

    # Adress
    sam.change_address(
        "Coola Gatan 32",
        "765 43",
        "Las Vegas"
    )
    
    # Byte av address
    sexig_brud.change_address(
        sam.address,
        sam.zipcode,
        sam.city
    )
    
    print(
        f"{sam.birthdate} - {sam_age} år gammal\n"
        f"{sam.name}\n"
        f"{sam.address}\n"
        f"{sam.zipcode}\n"
        f"{sam.city}\n"
    )

    print(
        f"{sexig_brud.birthdate} - {sexig_age} år gammal\n"
        f"{sexig_brud.name}\n"
        f"{sexig_brud.address}\n"
        f"{sexig_brud.zipcode}\n"
        f"{sexig_brud.city}\n"
    )
