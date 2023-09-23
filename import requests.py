import requests
import pandas as pd
import json
import datetime 
URL = "http://20.244.56.144/train/trains"
Token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTU0NTczNjcsImNvbXBhbnlOYW1lIjoiMjBKNDFBNjY0OSIsImNsaWVudElEIjoiM2U0NTVlZmEtMDM1NC00M2Y1LTljMmMtOGY5YjVjNTFlNWZiIiwib3duZXJOYW1lIjoiIiwib3duZXJFbWFpbCI6IiIsInJvbGxObyI6IjIwSjQxQTY2NDkifQ.PZRCbIy7IsAv2r4AhHWeOjT-_bx2U1dvuy4eJUXGZ9c"
if __name__ == "__main__":
    headers = {
        "Authorization":"Bearer {token}".format(token=Token)
	}
    curtime = datetime.datetime.now()
    print(curtime)
    r = requests.get(URL,headers=headers)
    data = r.json()
    #print(data)
    train_name = []
    train_number=[]
    departureTime = []
    seatsAvailable = []
    price = []
    delayedBy = []
    for i in data:
        curtime += datetime.timedelta(minutes=30)
        #print(curtime)
        if int(curtime.minute) < i['departureTime']["Minutes"] and int(curtime.hour) < i['departureTime']["Hours"]:
                        train_name.append(i["trainName"])
                        train_number.append(i["trainNumber"])
                        departureTime.append(i["departureTime"])
                        seatsAvailable.append(i["seatsAvailable"])
                        price.append(i["price"])
                        delayedBy.append(i["delayedBy"])

    print(train_name,train_number,departureTime,seatsAvailable,price,delayedBy)
    tabledict = {"train_name":train_name,"train_number":train_number,
    "departureTime":departureTime,
    "seatsAvailable":seatsAvailable,
    "price":price,
    "delayedBy":delayedBy}
    tablelist = pd.DataFrame(tabledict,columns = ["train_name","train_number",
    "departureTime",
    "seatsAvailable",
    "price",
    "delayedBy"])
    print(tablelist)
    