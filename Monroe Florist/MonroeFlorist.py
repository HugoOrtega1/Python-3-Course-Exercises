#Hugo Ortega     Monroe Florist   

def add(*totalAmount):
    total = 0
    print(totalAmount)
    for amount in totalAmount:
        total = total + amount
    return(total)

tax=7.25
Continue = 0
runningTotal = 0
hitCounter=0  


fType=[]
fColor=[]



shop_inventory= {
        "roses": {
                "price":25,
                "colors":["red","yellow","pink"]},
        "Marigolds": {
                "price":15,
                "colors":["orange","red","purple"]},
        "Lilies": {
                "price":20,
                "colors":["white","yellow","purple","orange"]},
        "daises": {
                "price":12,
                "colors":["yellow"]}
        } 

def get_color(name,flower):
    
    print(f'{name}! Great Selection, now chose a color. {name} come in ',*flower["colors"])
    
    color = str(input("what color would you like?")).capitalize()
    return flower["price"],color

print('Welcome to Monroe Florist, we have a wide varitey of flowers and colors to choose from. We also have a delivery option as well as a special card addon to make the special event even more memorable. Our curent selections of flowers are, Roses, Daisies, Marigolds and lilies Monroe florist only sells flowers by the dozen. Prices are as goes,Please select from the following:', '\n', 'Roses = $25', '\n', 'Daisies = $12' , '\n', 'Marigolds = $15', '\n','Lilies = $20' )

while Continue != "No":
    try:
        flowerType=str(input('Enter Flower type you would like to purchase:')).capitalize()
        fType.append(flowerType)
        hitCounter=hitCounter+1
    except Exception:
        print("something went wrong, please try again")
    if flowerType == "Roses":
        flowerPrice, flowerColor = get_color("Roses",shop_inventory['roses'])
        fColor.append(flowerColor)
        
    elif flowerType == "Daisies":
        flowerPrice, flowerColor = get_color("Daises",shop_inventory['daises'])
        fColor.append(flowerColor)
    elif flowerType == "Marigolds":
        flowerPrice, flowerColor = get_color("Marigolds",shop_inventory['Marigolds'])
        fColor.append(flowerColor)
    elif flowerType == "Lilies":
        flowerPrice, flowerColor = get_color("Lilies",shop_inventory['Lilies'])
        fColor.append(flowerColor)
    else:
        print("Invalid option, please Try again")
        break
    try:
        cardAddon=str(input("Would you like to add a gift card for an extra $0.50?")).capitalize()
    except Exception:
        print("something went wrong, please try again")
    
    if cardAddon == "Yes":
        cardAddon=0.50
    elif cardAddon == "No":
        cardAddon=0
    else:
        print("Invalid selection, please try Again.")
        break
    
    try:   
          delivery=str(input('Would you like standard delivery?')).capitalize()
    except Exception:
        print("something went wrong, please try again")
    
    if delivery == "Yes": 
        print("Thank you for choosing standard delivery")
        deliveryName=str(input('What is the name of the person to who we will deliver?')).capitalize()
        deliveryAddress=str(input('What is the delivery Address?'))
        billingName=str(input('ok, now What is the billing name?')).capitalize()
        billingAddress=str(input('What is the billing Address?'))

        runningTotal = add(flowerPrice+cardAddon, runningTotal+(runningTotal * 0.725))
        
        Continue=input("would you like to place another order?:").capitalize()
        
    elif delivery == "No":
        billingName=str(input('Ok,What is the billing name?')).capitalize()
        billingAddress=str(input('What is the billing Address?'))
        runningTotal = add(flowerPrice+cardAddon, runningTotal+(runningTotal * .0725))
    
        Continue=input("would you like to place another order?:").capitalize()
        print("Here is the current transaction details for {} , residing in {}. You have requested a total of {} dozens of flowers. you ordered {}  totaling {}".format(billingName,billingAddress,hitCounter,flowerType,runningTotal))
        
    else:
        print("Invalid selection, please try again")
        
 
input("please press Enter to close")
        
        
        
        
        
        
        
        
    












