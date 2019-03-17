from selenium import webdriver
import time

data = [['Himanshu Muit',547],['Abhishek Muit',5473],['Madhvi',652],["Jigyasa",45875]]
import pandas
import numpy as np
df = pandas.DataFrame(data,columns=['Name','amt'])

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
    msg = 'Hello, ' + i + ' You have to pay' + str(df["amt"][a]) + 'Rs'
    print('Enter anything after scanning QR code')
   # print(name)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
