import csv
from shopkeeper.models import ContainmentZone

f = open('containment.csv','r')

reader = csv.reader(f)
i = 0
for row in reader:
	if(row[1]!='District'):
		_,obj = ContainmentZone.objects.get_or_create(district=row[1],localbody=row[2],wardnum=row[4])
		i=i+1
		print(i)