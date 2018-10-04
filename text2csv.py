import csv;
numbers = """Zaika:+919116666156
Yo Zing:+917983653992
ChaapHut:+919950699999
Tea Tradition: +917340000547
Tandoor:+911416530007
Saras:+917357549601
Login:+919116666156
Let's Go Live:+917742603072
Kebab Nation:+919983087222
HealthBar:+917073991323
Dev Sweets and Snacks:+919001641663
Delight:+917240422018
Cruncheezz:+917665423182
Crazy Chef:+919521099336
Chilling point:+919351516665
Chatkara:+917983653992
Cafe Dialog:+917229906333"""

for number in numbers.split('\n'):
    print(number)
    k,v = number.split(':')
    with open('./day.csv', 'a', newline = '') as day:
        writer = csv.writer(day, delimiter = ',')
        writer.writerow([k,v])
