light_color="red"
car_detected=True

if light_color=="red" and car_detected==False:
    print("Do Nothing!")
elif light_color=="red" and car_detected==True:
    print("Flash!")
elif light_color=="green" and car_detected==True:
    print("nothing")
elif light_color=="green" and car_detected==False:
    print("nothing")
elif light_color=="Amber" and car_detected==True:
    print("nothing")
elif light_color=="Amber" and car_detected==False:
    print("nothing")
else: 
    print("all good!")