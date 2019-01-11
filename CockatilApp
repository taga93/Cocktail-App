
class Cocktail:  #class for creating cocktails
    
    def __init__(self, name, ingredients):

        self.name = name
        self.ingredients = ingredients

    def cockatil_Info(self): #get information about specific cocktail
        
        print(self.name.title().strip(),":")

        for liquor in self.ingredients:
            print(" -",liquor.title().strip())

    def __str__(self):
        return "{} | {}\n".format(self.name, self.ingredients)

        
JuiceVodka = Cocktail("Juice Vodka",["Orange Juice","Vodka"])
GinTonic = Cocktail("Gin Tonic",["Gin","Tonic"])
RumCola = Cocktail("Rum Cola",["Rum","Coca Cola"])
WhiskyCola = Cocktail("Whisky Cola",["Whisky", "Coca Cola"])

#___________________________________________________________________________________

class Cocktail_Bar:  #class for cocktail bars

    def __init__ (self, name):

        self.barthender = []

        self.name = name
        self.drinks = ["Vodka", "Gin", "Rum", "Tequila", "Whisky", "Curracao blue", "Beer",
                       "Amaretto", "Triple Sec", "Coca Cola", "Fanta", "Sprite", "Red Bull", "Tonic",
                       "Orange Juice", "Blueberry Juice","Grenadine", "Pineapple Juice", "Lemon Juice"]

        self.cocktails = [JuiceVodka, GinTonic, RumCola, WhiskyCola]



    def all_cocktails(self): #show all cocktails that bar has

        i = 0
        print(len(self.cocktails), "different cocktails.")
    
        for cocktail in self.cocktails:
            i+=1
            print("\n", i,")", cocktail.name)

            for liquor in cocktail.ingredients:
                print("    -", liquor)

                

    def get_cocktail(self, name): #get specific cocktail

        name = name.strip().lower()

        for cocktail in self.cocktails:

            if cocktail.name.lower() == name:
                print("\n",cocktail.name)
                
                for liquor in cocktail.ingredients:
                    print(" -", liquor)
                break

        else:
            print("There is no cocktail named", name.title())



    def cocktail_Names(self):   # show names of all cocktails
        
        i = 0
        print(len(self.cocktails), "different cocktails.\n")
    
        for cocktail in self.cocktails:
            i+=1
            print( i,")", cocktail.name)



    def all_needed_ingredients(self):   # show all ingredients for all cocktails

        all_needed_drinks = []

        for cocktail in self.cocktails:
            for liquor in cocktail.ingredients:

                if liquor.lower() not in all_needed_drinks:
                    all_needed_drinks.append(liquor.lower())

        print("You need",len(all_needed_drinks),"different drinks for all cocktails.\n")
        i=0
        for drink in all_needed_drinks:
            i += 1
            print(i, ")", drink.strip().title())



    def add_new_cocktail(self, name, drinks):   #add new cocktail to bar menu

        name = name.lower().strip()
        cocktail_dinks = []

        for cocktail in self.cocktails:
            if cocktail.name.lower()==name:
                print("Cocktail",name.title(),"already in list")
                
            else:
                for drink in drinks:
                    cocktail_dinks.append(drink.strip().title())
                    
                new_cocktail = Cocktail(name.strip().title(), cocktail_dinks)
                self.cocktails.append(new_cocktail)
                
                print("Cocktail named",new_cocktail.name,"added!\n")
                break



    def delete_Cocktail(self, name):  #delete specific cocktail

        for cocktail in self.cocktails:
            if cocktail.name.lower()== name.lower().strip():
                
                self.cocktails.remove(cocktail)
                print("Cocktail",name.title(),"deleted!\n")
                break

        else:
            print("There is no cocktail named", name.title(),"!")



    def shopping(self):  #show what ingredients you need to buy so that you can make all cocktails 

        Needed_Drinks = []
        for cocktail in self.cocktails:
            for liquor in cocktail.ingredients:

                if liquor.strip().lower() not in Needed_Drinks:
                    Needed_Drinks.append(liquor.strip().lower())


        Bar_Drinks = []
        for drink in self.drinks:
            Bar_Drinks.append(drink.strip().lower())


        missing_drinks = set(Needed_Drinks) - set(Bar_Drinks)


        if len(missing_drinks) != 0:
            print("\nYou need to buy:")

            for drink in missing_drinks:
                print("  -", drink.strip().title())
                
        else:
            print("\nYou have all drinks!")



    def search_by_liquor(self, drinks): #show cocktails that has specific liquor
        print("\nCocktails that have specific liquor/s:")

        i=0
        for cocktail in self.cocktails:
            for drink in drinks:
                
                if drink.lower() in (liquor.lower() for liquor in cocktail.ingredients):
                    i+=1
                    print("\n", i,")", cocktail.name.title(), "\n")
                    
                    for cocktail_ingredients in cocktail.ingredients:
                        print("  -",cocktail_ingredients.title())


    def what_can_i_make(self, all_drinks):  #enter list of ingredients and see what coctails can you make

        all_drinks_set = set()
        for item in all_drinks:
            all_drinks_set.add(item.strip().lower())

        print("\nAvailable cocktails:")
        
        i=0
        for cocktail in self.cocktails:
            new_cocktail = set(drink.strip().lower() for drink in cocktail.ingredients)

            if new_cocktail.intersection(all_drinks_set) == new_cocktail:

                i+=1
                cocktail_Name = str(cocktail.name.strip().title())
                print("\n",i,")", cocktail_Name,"\n")
            
                for cocktail_ingredients in cocktail.ingredients:
                    print("  -",cocktail_ingredients.strip().title())

        else:
            print("No available cocktails!")



myBar = Cocktail_Bar("My Tropical Bar")
#myBar.all_cocktails()
#myBar.get_cocktail("Juice vottdka")
#myBar.cocktail_Names()
#myBar.all_needed_ingredients()
#myBar.add_new_cocktail("Taga",["Pelinkovac ", " coca cola"])
#myBar.all_cocktails()
#myBar.all_needed_ingredients()
#myBar.delete_Cocktail("Gin Tonic")
#myBar.all_cocktails()
#myBar.all_needed_ingredients()
#myBar.search_by_liquor(["gin","coca cola"])
#myBar.what_can_i_make(["tonic","rum"])
#myBar.shopping()











