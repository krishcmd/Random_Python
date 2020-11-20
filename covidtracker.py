from covid import Covid
import matplotlib.pyplot as plt

covid = Covid()
#clist= covid.list_countries()
#print(clist)
while True:
	name = input("\nEnter the country name: ")

	virusdata = covid.get_status_by_country_name(name)
	remove = ['id','country','latitude','longitude','last_update']

	for i in remove:
		virusdata.pop(i)

	confirmedcases = virusdata.pop('confirmed') 

	id = list(virusdata.keys());
	value = [str(i) for i in virusdata.values()]

	plt.pie(value, labels = id, colors = ['r','y','g','b'], autopct= '%1.1f%%')
	plt.title("COUNTRY: "+name.upper() +"\n TOTAL CASES: "+str(confirmedcases))
	plt.show()
	repeat=input("Do you want to continue? :(Y/N)").capitalize()

	if "Y" in repeat:
		continue
	else:
		exit()
