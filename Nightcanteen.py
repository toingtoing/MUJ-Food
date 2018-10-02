##nc=open('./NightCanteen.txt')
##print("Night Canteen List")
##print("1. Cafe Dialog \n2. Kebab Nation \n3. Login \n4. Saras")
##res=input("\nEnter Night Canteen Hotel Name \n")
##res=res.lower()
##name=list(res)
##for line in nc:
##    for letter in line:
##        if letter==name[0]:
##            print(line)
##        else:
##            break
##nc.close()

import csv

def main():
    
    print('Your Options Are: \n1.night canteen \n2.day canteen')
    selection = input('Select the corresponding number: ')
    print('*'*10)

    try:
        selection = int(selection)

    except ValueError:
        print("Enter a number!")
        return 0

    if selection > 2 | selection < 0:
        print('Enter a valid input')
        return 0

    elif selection == 1:
        print("Night Canteen List")
        print('*'*10)
        with open('./night.csv', 'r') as night:
            reader = csv.reader(night)
            data = {row[0]: row[1] for row in reader}
            for item in data:
                print(item)
                
                
        res=input("\nEnter Night Canteen Hotel Name:\n").lower()
        for rows in data:
            if res[0] == rows[0].lower():
                print(str(rows) + ':' + data[rows])

    elif selection == 2:
        print("Day Canteen List")
        print('*'*10)
        with open('./day.csv', 'r') as night:
            reader = csv.reader(night)
            data = {row[0]: row[1] for row in reader}
            for item in data:
                print(item)
                
                
    ##    print(data)
        res=input("\nEnter Day Canteen Hotel Name:\n").lower()
        for rows in data:
            if res in rows.lower():
                print(str(rows) + ':' + data[rows])
            


if __name__ == "__main__":
    main()

    
    
