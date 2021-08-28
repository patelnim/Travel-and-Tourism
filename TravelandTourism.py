print("|---------------------------------------------------------------------------------------------------------------------------------------------|")
print("|                                                                                                                                             |")
print("|                                                  *WELCOME TO DREAM WORLD HOLIDAYS*                                                          |")
print("|                                           Travel brings power and love back into your life                                                  |")
print("|                                                                                                                                             |")
print("|---------------------------------------------------------------------------------------------------------------------------------------------|")
print(" ")
print("ABOUT US")
print(" ")
print("Dreams are successions of images, ideas, emotions, and sensations that occur usually involuntarily in the mind .")
print("The fulfillment of all of our dreams begins with intention and desire. … ")
print("Here are we “DREAM WORLD HOLIDAYS” for cultivating and fulfilling your Tour intentions with grace and ease.")
print("We are passionately committed to deliver quality travel and numerous attractive Low budget package tours with professionalism and warmth.")
print("The fact is that moving from place to place is really fascinating.")
print("Travel is an important diversion for us from daily mundane routine.")
print("Alternative traveling enables intense experiences that  happen while traveling in an all-inclusive tourist package.")
print("It also promotes friendship  and prejudice while experiencing other cultures from ”inside”. ")
print("The BEAUTY of NATURE always brings amazing INNER PEACE for human.")
print(" ")
print("Come let us celebrate & explore dreams to reality through “DREAM WORLD HOLIDAYS“.")
print(" ")
print(" ")
print(" ")
a=input("Enter your Name:")
print(" ")
b=input("Enter your Age:")
print(" ")
while True:
    c=input("Enter your contact Number:")
    if len(c)==10:
        break
    else:
        print("Please Enetr 10 digit number:")
        continue
print(" ")
a=input("Enter your Email id:")
print(" ")
print("Thank you for sharing your details")
print("Feel free to query us on ")
print("DREAM WORLD HOLIDAYS")
print("Add:Block:101,3rd floor,Andheri")
print("Contact no:0987654321,1234567890")
print("email:dreamworldholidays@gmail.com ")
print("WE ENSURE YOU FOR BEST SERVICES!!!")
print(" ")
print("Here are some List of Travel Places")
print("|----------------------------------|")
print("|----------------------------------|")
print("|   1)Kashmir                      |")
print("|                                  |")
print("|   2)Shimla_Manali                |")
print("|                                  |")
print("|   3)Darjeeling_Gangtok           |")
print("|                                  |")
print("|   4)Kerala                       |")
print("|                                  |")
print("|   5)OOTY_Mysore                  |")
print("|                                  |")
print("|----------------------------------|")
print("|----------------------------------|")
print(" ")
print(" ")
f=True
while f==True:
    e=input("Enter the city you want to visit from the Travel list:")
    if e=='1':
        print(" ")
        print("For 3 Night 2 days:\n HOTEL: Hotel Tropical\n Houseboat Summit Grand\n PLACES:\n *Gulmarg\n *Sonmarg\n *Pahalgam\n *Dal Lake\n *Srinagar Local\n Total Package:21,000\n****" )
    elif e=='2':
        print(" ")
        print("For 3 Night 2 days:\n HOTEL: Hotel Snow Palace\n Hotel Woodland\n PLACES:\n *Kufri\n *Jakhoo Temple\n *Rohtang Pass\n *Mannikaran\n *Vashsit Kund,Hidimba Temple\n Total Package:24,000\n****" )
    elif e=='3':
        print(" ")
        print("For 3 Night 2 days:\n HOTEL: Hotel Gangtok Heights\n Hotel Pinetree\n PLACES:\n *Tsomgo Lake & Baba Mandir\n *Nathu La Pass\n *Tiger Hill \n *Ghoom Monastery and Batasia Loop\n *Padmaja Naidu Zoological Park, Himalayan Mountaineering Institute\n Total Package:52,000\n****" )
    elif e=='4':
        print(" ")
        print("For 3 Night 2 days:\n HOTEL: Hotel Dunes\n Hotel Dale\n PLACES:\n *Cochi\n *Munnar\n *Thekkady \n *Alleppy Houseboat\n *Kovlam\n Total Package:35,000\n****" )
    elif e=='5':
        print(" ")
        print("For 3 Night 2 days:\n HOTEL: Hotel Vrindavan\n Hotel Lakeview\n PLACES:\n *Mysore Palace\n *Brindavan Gardens & Mysore Zoo\n *OOty Boat House,Toy train \n *Botanical Garden,Rose Garden\n *Doddabetta Peak\n *Mudumalai National Park\n Total Package:55,000\n****" )
    else:
        print(" ")
        print("You have entered an incorrect option,please try it again")
    print(" ")
    g=input("Do you want to repeat YES/NO :").lower()
    if g=="yes":
       continue
    elif g=='no':
       break
    else:
        print("Invalid input please try again")
print('1)For Payment\n 2) for inquiry')
print(" ")
h=input("Eneter your choice 1 or 2 :")
print(" ")
if h=='1':
    j=input("Enter the number of person:")
    print(" ")
    r=input("Enter your full address (with city):")
    print(" ")
    s=input("Enter the mode of Transportation you prefer(Train or Aeroplane):")
    print(" ")
    i=input("Enter the city number you want to visit :")
    if i=='1':
        print("For Kashmir TotalPackage for 3n4 days is Rs 21,000 and for 5n 6days is 31,000(Children under age 5 are Free)")
        first=j*21,000
        first2=j*31,000
    elif i=='2':
        print("For Shimla_Manali Total Package for 3n4days is Rs 24,000 and for 5n 6days is 34,000(Children under age 5 are Free)")
        first=j*24,000
        first2=j*34,000
    elif i=='3':
        print("For Darjeeling_Gangtok Total Package for 3n 4days is Rs 52,000 and 5n 6 daysis 62,000(Children under age 5 are Free)")
        first=j*52,000
        first2=j*62,000
    elif i=='4':
        print("For Kerala Total Package for 3n 4days is Rs 35,000 and for 5n 6 days is 45,000(Children under age 5 are Free)")
        first=j*35,000
        first2=j*45,000
    elif i=='5':
        print("For OOTY_Mysore Toatal Package for 3n 4days is Rs 55,000 and for 5n 6days is 65,000(Children under age 5 are Free)")
        first=j*55,000
        first2=j*65,000
    else :
        print("Please enter the correct option")
    print(" ")
    print("Please enter your card information.")
    print(" ")
    k=input("Enter the card holder name:")
    print(" ")
    while True:
        l=input("Enter Card number:")
        if len(l)==12:
            break
        else:
            print("Please Enter 12 digit Card Number")
            continue
    print(" ")
    m=input("Enetr Exp Date (mm/yyyy):")
    while True:
        n=input("Enter CVV number:")
        if len(n)==3:
            break
        else:
            print("Please Eneter 3 digit cvv number")
            continue
    print(" ")
    print("Total Cost you will get from",s,"for 3 n 4 Days is ",first,"and for 5n 6 Days is" ,first2)
    print(" ")
    p=input("Enter the number of days you want to go for trip(3 or 5):")
    if p=='3':
        q=first
    elif p=='5':
        q=first2
    while True:
        o=input("Do you want to make payment (yes/no)").lower()
        if o=='yes':
            print(j,"number of person are going for",p,"days from",r,"in",s,". with a total cost of ",q,"\n Your Transactin has been successful\n Kindly check your email for Package and Ticket details\n Thank you")
            break
elif h=='2':
        print("This is DREAM WORLD HOLIDAYS.Do your give feed back or Feel free to query us on \n Add:Block:101,3rd floor,Andheri \n Contact no:0987654321,1234567890 \n email:dreamworldholidays@gmail.com \n WE ENSURE YOU FOR BEST SERVICES!!! ")
             
