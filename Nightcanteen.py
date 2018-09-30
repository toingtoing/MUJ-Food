nc=open('/home/prajay/Documents/NightCanteen.txt')
print("Night Canteen List")
print("1. Cafe Dialog \n2. Kebab Nation \n3. Login \n4. Saras")
res=input("\nEnter Night Canteen Hotel Name \n")
res=res.lower()
name=list(res)
for line in nc:
    for letter in line:
        if letter==name[0]:
            print(line)
        else:
            break
nc.close()
