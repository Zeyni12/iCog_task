#my bag is only take 10kg, so how much vegetable should i take to maximaize my profit/value
#i use a greedy method so first i list my vegitable, value/profit and weight  
items=[('onion',7,3),('potato',4,1),('tomato',6,2),('cucumber',2,1),('green chili',3,0.5),('spinach',1,0.5),('carrot',5,2),]

def vegetable_bag(items,capacity):
    
    items = sorted (items, key=lambda item:item[1]/item[2],reverse=True)#it sorted based on value/profit divided to weight of the vegetables 
    chosen_vegetable ={}
    profit = 0
    for i in range(len(items)):
        vegetable,value,weight = items[i]
        num_of_vegetable = (capacity - capacity % weight)/weight
        chosen_vegetable[vegetable] = num_of_vegetable
        capacity = capacity % weight
        profit += num_of_vegetable*value
    return round(profit,2),chosen_vegetable
print(vegetable_bag(items,10))    
   



