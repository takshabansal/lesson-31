class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is a developing country")
class United_States_of_America():
    def capital(self):
        print("Washington D.C. is the capital of United_States_of_America")
    def language(self):
        print("English(American, not british) is the most widely spoken language of United_States_of_America")
    def type(self):
        print("United_States_of_America is a developed country")
class Russian_Federation():
    def capital(self):
        print("Moscow is the capital of the Russian_Federation")
    def language(self):
        print("Russian is the most widely spoken language of the Russian_Federation")
    def type(self):
        print("The Russian_Federation is a war waging nuclear developed country")
obj_ind=India()
obj_usa=United_States_of_America()
obj_rus=Russian_Federation()
for country in (obj_ind, obj_usa, obj_rus):
    country.capital()
    print()
    country.language()
    print()
    country.type()
    print()