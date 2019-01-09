from abc import ABC, abstractmethod


class Coctail:  #class for creating coctails
    
    def __init__(self, name, ingredients):

        self.name = name
        self.ingredients = ingredients

    def cocatil_Info(self): #get information about specific coctail
        
        print(self.name.title().strip(),":")

        for liquor in self.ingredients:
            print(" -",liquor.title().strip())

    def __str__(self):
        return "{} | {}\n".format(self.name, self.ingredients)

        
JuiceVodka = Coctail("Juice Vodka",["Orange Juice","Vodka"])
GinTonic = Coctail("Gin Tonic",["Gin","Tonic"])
RumCola = Coctail("Rum Cola",["Rum","Coca Cola"])
WhiskyCola = Coctail("Whisky Cola",["Whisky", "Coca Cola"])

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
    
    def __init__(self, first_name, last_name, salary, coctails):
        super().__init__(first_name, last_name, salary)

        self.coctails = coctails


    def add_coctail(self, new_coctail_name, new_coctail_ingredients):#add coctail that bartender can make

        ingredients = []

        for drink in new_coctail_ingredients:
            drink = drink.strip().title()
            ingredients.append(drink)

        new_Coctail = Coctail(new_coctail_name.strip().title(), ingredients)

        if new_Coctail.name.strip().title() not in self.coctails:
            self.coctails.append(new_Coctail)
            print("\nCoctail named", new_Coctail.name.strip().title(), "added!")
        else:
            print("\nCoctail", new_Coctail.name.strip().title(), "already in list!")


    def coctail_list(self): #get all coctails that bartender can make

        print("\n", self.first_name, self.last_name,"makes:")
        i=0
        if not self.coctails:
            print("\n0 coctails.")
        else:
            for coc in self.coctails:
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
print(BarEmployee)

#BarEmployee.employee_info()
#BarEmployee.coctail_list()
#BarEmployee.add_coctail("taga",[" pelinkovac  ", "Coca cola "])
#BarEmployee.coctail_list()
#BarEmployee.apply_raise(10)
#BarEmployee.set_salary(33000)
#BarEmployee.monthly_salary()

#__________________________________________________________________________
    

class Coctail_Bar:  #class for coctail bars

    def __init__ (self, name):

        self.barthender = []

        self.name = name
        self.drinks = ["Vodka", "Gin", "Rum", "Tequila", "Whisky", "Curracao blue", "Beer",
                       "Amaretto", "Triple Sec", "Coca Cola", "Fanta", "Sprite", "Red Bull", "Tonic",
                       "Orange Juice", "Blueberry Juice","Grenadine", "Pineapple Juice", "Lemon Juice"]

        self.coctails = [JuiceVodka, GinTonic, RumCola, WhiskyCola]



    def all_coctails(self): #show all coctails that bar has

        i = 0
        print(len(self.coctails), "different coctails.")
    
        for coctail in self.coctails:
            i+=1
            print("\n", i,")", coctail.name)

            for liquor in coctail.ingredients:
                print("    -",liquor)

                

    def get_coctail(self, name): #get specific coctail

        name = name.strip().lower()

        for coctail in self.coctails:

            if coctail.name.lower() == name:
                print("\n",coctail.name)
                
                for liquor in coctail.ingredients:
                    print(" -", liquor)
                break

        else:
            print("There is no coctail named", name.title())



    def coctail_Names(self):   # show names of all coctails
        
        i = 0
        print(len(self.coctails), "different coctails.\n")
    
        for coctail in self.coctails:
            i+=1
            print( i,")", coctail.name)



    def all_needed_ingredients(self):   # show all ingredients for all coctails

        all_needed_drinks = []

        for coctail in self.coctails:
            for liquor in coctail.ingredients:

                if liquor.lower() not in all_needed_drinks:
                    all_needed_drinks.append(liquor.lower())

        print("You need",len(all_needed_drinks),"different drinks for all coctails.\n")
        i=0
        for drink in all_needed_drinks:
            i += 1
            print(i, ")", drink.strip().title())



    def add_new_coctail(self, name, drinks):   #add new coctail to bar menu

        name = name.lower().strip()
        coctail_dinks = []

        for coctail in self.coctails:
            if coctail.name.lower()==name:
                print("Coctail",name.title(),"already in list")
                
            else:
                for drink in drinks:
                    coctail_dinks.append(drink.strip().title())
                    
                new_coctail = Coctail(name.strip().title(), coctail_dinks)
                self.coctails.append(new_coctail)
                
                print("Coctail named",new_coctail.name,"added!\n")
                break



    def delete_Coctail(self, name):  #delete specific coctail

        for coctail in self.coctails:
            if coctail.name.lower()== name.lower().strip():
                
                self.coctails.remove(coctail)
                print("Coctail",name.title(),"deleted!\n")
                break

        else:
            print("There is no coctail named", name.title(),"!")



    def shopping(self):  #show what ingredients you need to buy so that you can make all coctails 

        Needed_Drinks = []
        for coctail in self.coctails:
            for liquor in coctail.ingredients:

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



    def search_by_liquor(self, drinks): #show coctails that has specific liquor
        print("\nCoctails that have specific liquor/s:")

        i=0
        for coctail in self.coctails:
            for drink in drinks:
                
                if drink.lower() in (liquor.lower() for liquor in coctail.ingredients):
                    i+=1
                    print("\n", i,")", coctail.name.title(), "\n")
                    
                    for coctail_ingredients in coctail.ingredients:
                        print("  -",coctail_ingredients.title())


    def what_can_i_make(self, all_drinks):  #enter list of ingredients and see what coctails can you make

        all_drinks_set = set()
        for item in all_drinks:
            all_drinks_set.add(item.strip().lower())

        print("\nAvailable coctails:")
        
        i=0
        for coctail in self.coctails:
            new_coctail = set(drink.strip().lower() for drink in coctail.ingredients)

            if new_coctail.intersection(all_drinks_set) == new_coctail:

                i+=1
                coctail_Name = str(coctail.name.strip().title())
                print("\n",i,")", coctail_Name,"\n")
            
                for coctail_ingredients in coctail.ingredients:
                    print("  -",coctail_ingredients.strip().title())

        else:
            print("No available coctails!")



myBar = Coctail_Bar("My Tropical Bar")
#myBar.all_coctails()
#myBar.get_coctail("Juice vottdka")
#myBar.coctail_Names()
#myBar.all_needed_ingredients()
#myBar.add_new_coctail("Taga",["Pelinkovac ", " coca cola"])
#myBar.all_coctails()
#myBar.all_needed_ingredients()
#myBar.delete_Coctail("Gin Tonic")
#myBar.all_coctails()
#myBar.all_needed_ingredients()
#myBar.search_by_liquor(["gin","coca cola"])
#myBar.what_can_i_make(["tonic","rum"])
#myBar.shopping()











