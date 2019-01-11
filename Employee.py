from abc import ABC, abstractmethod

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
