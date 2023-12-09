Hotels_in_Krakow = [
{"name":"Sky","price":320.00},
{"name":"Metropol","price":480.00},
{"name":"New Port","price":420.00},
{"name":"Aparthotel","price":390.00}
]
Hotels_in_Sopot = [
{"name":"Focus","price":510.00},
{"name":"Aqua","price":345.00},
{"name":"La Boutique","price":390.00},
{"name":"Marina","price":410.00}
]

print()

def hotel_list(hotels):
    sum =""
    for x in hotels:
        sum +=x["name"]+ ', '
    return f'Hotels: {sum}'
        

#print(hotel_list(Hotels_in_Krakow))
def avg_price(hotels, name):
    sum = 0
    count= 0
    for x in hotels:
        sum +=x["price"]
        count += 1
    avg = sum/count
    return f'Average hotel price in {name}: {int(avg)}'

#print(avg_price(Hotels_in_Krakow))


def comparison(fac1,n1,fac2,n2):
    if avg_price(fac1,n1)>avg_price(fac2,n2):
        name = "Krakow"
    elif avg_price(fac1,n1)<avg_price(fac2,n2):
        name = "Sopot"
    elif avg_price(fac1,n1)==avg_price(fac2,n2):
        name = "average prices are aqual"
    return f'Cheaper hotels in: {name}'

if __name__=="__main__":
    print(hotel_list(Hotels_in_Krakow))
    print(avg_price(Hotels_in_Krakow, "Krakow"))
    print(comparison(Hotels_in_Krakow, "krakow", 
                     Hotels_in_Sopot,'Sopot' ))