import requests
from bs4 import BeautifulSoup
import csv

new_dict = dict
# source_page = requests.get('https://usda.library.cornell.edu/concern/publications/gm80hv35d')
# # print(source_page.status_code)
# # print(source_page.content)
# #
# #SOURCE NAME EXTRACTION
# soup = BeautifulSoup(source_page.content,'html.parser')
# soup.prettify()
# temp = soup.find_all(class_='col-xs-12 col-sm-9')
# new_temp = str(temp)
# source_names = (new_temp.split('\n'))
# print(source_names[1])
source_list =  [
                    'https://usda.library.cornell.edu/concern/publications/3t945q76s?locale=en',
                    'https://usda.library.cornell.edu/concern/publications/3t945q76s?locale=en',
                    'https://usda.library.cornell.edu/concern/publications/8336h188j',
                    'https://usda.library.cornell.edu/concern/publications/mp48sc77c',
                    'https://usda.library.cornell.edu/concern/publications/m326m174z',
                    'https://usda.library.cornell.edu/concern/publications/gm80hv35d',
                    'https://usda.library.cornell.edu/concern/publications/fb494842n',
                    'https://usda.library.cornell.edu/concern/publications/rj430453j'
               ]
fp = csv.writer(open('D:\Office_Scripts/notes.csv','w',encoding='utf-8'))
fields = ['Data Source Name','MM/DD/YYYY']
fp.writerow(fields)
for src in source_list:
    source_page = requests.get(src)
    # SOURCE NAME EXTRACTION
    soup = BeautifulSoup(source_page.content, 'html.parser')
    temp = soup.find_all(class_='col-xs-12 col-sm-9')
    new_temp = str(temp)
    source_names = (new_temp.split('\n'))


    # SOURCE LATEST RELEASE DATA EXTRACTION:
    source_parser = BeautifulSoup(source_page.content, 'html.parser')
    new_list = source_parser.find_all(class_='attribute date_uploaded')
    for row in new_list:
        for col in row:
            dates = source_names[1]
            dates = dates.strip()
            # # fp.write(dates)
            # fp.writerow(fields)
            fp.writerow([dates, col])
            # print(source_names[1] + " " +col)
            # fp.writerow(source_names[1] + col)
            # new_dict[source_names[1]] : col
        break

# fp.writerow(new_dict)

#Wrting Data to files
# fields = ['Data Source Name','MM/DD/YYYY']
# fp = csv.writer(open('D:\Office_Scripts/notes.csv','w',encoding='utf-8'))
#
# fp.writerow(fields)









#
# fields = ['Data Source Name','MM/DD/YYYY']
# fp = csv.writer(open('D:\Office_Scripts/notes.csv','w',encoding='utf-8'))
# for row in new_list:
#     for col in row:
#         dates = source_names[1]
#         dates = dates.strip()
#         # fp.write(dates)
#         fp.writerow(fields)
#         fp.writerow([dates,col])
#     break


