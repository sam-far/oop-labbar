class Kenneln:
    """
    Ett program som hanterar ett litet register över hundar 
    som finns på en kennel. För varje hund som registreras 
    skall finnas namn, ras, ålder och vikt.
    """
    
    def __init__(self, name, race, age, weight):
        """
        Initierar
        """
        self.name   = name
        self.race   = race
        self.age    = age
        self.weight = weight

    def registrera(self):
        """
        Registrera. Användaren får frågor om namn, 
        ras, ålder och vikt för hunden. Ett hundobjekt 
        skapas och läggs in i kennel-registret.
        """
        pass

    def lista(self):
        """
        Användaren får en fråga om minsta svanslängd och 
        programmet skriver ut en lista på alla hundar hos 
        kenneln som har längre svanslängd än denna minsta angivna 
        (om man anger 0 så kommer alltså alla hundar att skrivas ut, 
        anger man 10 så skrivs bara de hundarvars svanslängd>=10 ut).
        Svanslängden för en hund kan räknas ut med den fiffiga 
        formeln:svanslängden=åldern*vikten/10. Denna formel 
        gäller för alla hundar UTOM taxar. En tax har alltid 
        svanslängden 3.7. Vid utskriften skall alla hundens attribut 
        samt svanslängden skrivas ut, t.ex.Fido Pudel 4 år 7 kg 
        svans=2.8ellerNisse Tax 6 år 8 kg svans=3.7.
        """
        pass

    def ta_bort(self):
        """
        Användaren får en fråga efter namnet på hunden som 
        skall tas bort. Hunden meddet angivna namnet skall tas bort 
        ur kennel-registret. Om det inte finns någon hund med det 
        angivna namnet så skall programmet skriva utHund med det namnet 
        fanns ej i registretannars skall det skrivas utHunden med 
        det angivna namnet är borttagen. Nibehöverintetänka på 
        komplikationen att det kan finnas flera hundar med samma namn.
        """
        pass

    def avsluta(self):
        """
        Programmet avslutas. En tråkig effekt är att när programmet 
        avslutas så "försvinner" allt lagrat data (objekt som skapas 
        ligger i primärminnet och finns bara så länge programmet körs). 
        Alla registrerade hundar försvinner alltså... så den som 
        hinner – SPARA alla hundar i en fil som läses upp vid uppstart.
        """
        pass

if __name__ == "__main__":

    def kommandon():
        """
        Programmet skall vara kommandostyrt och fyra olika kommandon 
        skall kunna ges: namn, ras, ålder och vikt
        """
        name   = input("Namn: ")
        race   = input("Ras: ")
        age    = input("Ålder: ")
        weight = input("vikt: ")

        dog = Kenneln(name, race, age, weight)
        print(dog.name, dog.race, dog.age, dog.weight)

kommandon()