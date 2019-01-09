from abc import ABC, abstractmethod


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

class Employee(ABC): #abstract class for creating employees

    @abstractmethod
    def __init__(self, first_name, last_name, salary):

        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = (first_name + "_" + last_name + "@email.com").lower()

    @abstractmethod
    def employee_info(self):    #info about employees
        pass

    @abstractmethod
    def apply_raise(self, raise_percent): #raise employee's salary
        pass

    @abstractmethod
    def set_salary(self, salary): #set salary
        pass

    @abstractmethod
    def monthly_salary(self):   #get monthly salary
        pass
    
    @abstractmethod
    def __str__(self):
        pass



class Bartender(Employee):   #class for creating bartenders
    
    def __init__(self, first_name, last_name, salary, cocktails):
        super().__init__(first_name, last_name, salary)

        self.cocktails = cocktails


    def add_cocktail(self, new_cocktail_name, new_cocktail_ingredients):#add cocktail that bartender can make

        ingredients = []

        for drink in new_cocktail_ingredients:
            drink = drink.strip().title()
            ingredients.append(drink)

        new_Cocktail = Cocktail(new_cocktail_name.strip().title(), ingredients)

        if new_Cocktail.name.strip().title() not in self.cocktails:
            self.cocktails.append(new_Cocktail)
            print("\nCocktail named", new_Cocktail.name.strip().title(), "added!")
        else:
            print("\nCocktail", new_Cocktail.name.strip().title(), "already in list!")


    def cocktail_list(self): #get all cocktails that bartender can make

        print("\n", self.first_name, self.last_name,"makes:")
        i=0
        if not self.cocktails:
            print("\n0 cocktails.")
        else:
            for coc in self.cocktails:
                i +=1
                print(i, ")", coc)



    def employee_info(self):    #info about employees / bartender   (abs)
        
        return "\nName: {} {}\nContact: {}\n".format(self.first_name,
                                                   self.last_name,
                                                   self.email)

    def apply_raise(self, raise_percent): #raise employee's / bartender's salary (abs)

        raise_coef = raise_percent/100 + 1
        
        raise_amount =self.salary*raise_coef - self.salary
        self.salary = self.salary*raise_coef

        return "\nAnnual salary raised for: {}$ ({}%)\nAnnual salary after raise: {}$\n".format(round(raise_amount,2),
                                                                                              raise_percent,
                                                                                              round(self.salary, 2))

    def set_salary(self, salary): #set salary (abs)
        self.salary = salary
        print("\nSalary set to",self.salary,"$ per year.")

    def monthly_salary(self):   #get monthly salary  (abs)
        salary = self.salary / 12
        print("\nMonthly salary:",round(salary,2),"$")

    def __str__(self): #(abs)

        info = "\nName: {}\nLast name: {}\nContact: {}\nAnnual salary: {}$\n".format(self.first_name, self.last_name,
                                                                        self.email, self.salary)

        return info


BarEmployee = Bartender("Mike", "Jonson", 30000, [JuiceVodka, RumCola])
#print(BarEmployee)

#BarEmployee.employee_info()
#BarEmployee.cocktail_list()
#BarEmployee.add_cocktail("taga",[" pelinkovac  ", "Coca cola "])
#BarEmployee.cocktail_list()
#BarEmployee.apply_raise(10)
#BarEmployee.set_salary(33000)
#BarEmployee.monthly_salary()

#__________________________________________________________________________
    

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











