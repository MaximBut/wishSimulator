import random

class sumChancesException(Exception):
    def __init__(self, message): 
        super().__init__(message)
        
class wrongStructureException(Exception):
    def __init__(self, message, errorlist): 
        super().__init__(message)
        self.wrong_elements = []
        for i in range(len(errorlist)):
            if len(errorlist[i]) != 2:
                self.wrong_elements.append(f"Wrong element at index {i}: {errorlist[i]}")
                
    def __str__(self):
        return f"{self.args[0]}\n" + "\n".join(self.wrong_elements)
        
class impossibleChanceException(Exception):
    def __init__(self, message, errorlist): 
        super().__init__(message)
        self.wrong_elements = []
        for i in range(len(errorlist)):
            if len(errorlist[i]) <= 0:
                self.wrong_elements.append(f"Impossible chance at index {i}: {errorlist[i]}")
                
    def __str__(self):
        return f"{self.args[0]}\n" + "\n".join(self.wrong_elements)


def wish(wishlist):
    try:
        for item in wishlist:
            if (len(item)) != 2:
                raise wrongStructureException("Wrong structure of chance list:", wishlist)
         
         
        total_weight = sum(weight for _, weight in wishlist)
        
        if total_weight != 100:
            raise sumChancesException(f'Sum of chances is not equal to 100 ({total_weight} instead).')
        
        for item in wishlist:
            if item[1] <= 0:
                raise wrongStructureException("Impossible chance(s) found:", wishlist)
        
        
        selected = random.uniform(0, 100)
        sum_chance = 0
        for item, weight in wishlist:
            sum_chance += weight
            if selected <= sum_chance:
                return item
            
            
    except sumChancesException as sce:
        raise sce
    
    except wrongStructureException as wse:
        raise wse
    
    except impossibleChanceException as ice:
        raise ice