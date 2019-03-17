# import the libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas
from selenium import webdriver
import time

# link of google api
scope = ['https://www.googleapis.com/auth/drive']

#share your google api id
credentials = ServiceAccountCredentials.from_json_keyfile_name('Varun1997-9da040b1aea8.json',scope)
client = gspread.authorize(credentials)       # import data from google spreadsheet

# Open a Excel file like 'Project'
sheet = client.open('Project').sheet1

# get all data from the file
pp = pprint.PrettyPrinter()
data = sheet.get_all_records()

# Convert data in DataFrame format
df = pandas.DataFrame(data)

# give the chromedriver path
driver = webdriver.Chrome(r'C:\Users\Varun Jain\PycharmProjects\Basic\Data_Crawiling\drivers\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
time.sleep(6)

na = df['Name']
for i in na:
    name = i
    a = 0
    while a < na.count():
        if i == df['Name'][a]:
            break
        a += 1
    msg = 'Hello, ' + i + ' You have to pay ' + str(df['amt'][a]) + " Rs"
    print('Enter anything after scanning QR code')
   # print(name)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
