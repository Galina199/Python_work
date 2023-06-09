#Задание 44 
#В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
#Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


import random 
lst = ['robot'] * 10 
lst += ['human'] * 10 
random.shuffle(lst) 
data = pd.DataFrame(lst ,columns={'WhoAmI'}) 
data.head() 

# One hot вид (возможно так): 

data = pd.DataFrame(random.sample(['robot', 'human']*10, 10) ,columns={'WhoAmI'})  
data.head() 