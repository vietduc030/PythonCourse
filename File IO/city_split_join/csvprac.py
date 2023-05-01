city_list=[]

with open("city.csv","r") as file:
    
    for line in file:
       city_list.append(line.split(",")[0])

with open("city.txt","w") as file:
    file.write("\n".join(city_list[1:]))
    
    




