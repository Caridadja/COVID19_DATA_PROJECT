from csv import reader
opened_file = open("full_data.csv")
read_file = reader(opened_file)
data = list(read_file)
covid19_header = data[0]
covid19_footer = data[-1]
covid19_data = data[1:]
print(covid19_header)
def extract_data(country=input("Please insert country: ")):
	country_data = []
	for row in covid19_data:
		if row[1] == country:
			country_data.append(row)
	print("Total cases are: ",country_data[-1][4])
	print("Total deaths are: ",country_data[-1][5])
	print("Death rate is: ",round((int(country_data[-1][5]) / int(country_data[-1][4])) * 100, 2),"%")
	print("New cases are: ",country_data[-1][2])
extract_data()
