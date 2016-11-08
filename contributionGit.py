from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://github.com/users/ardyflora/contributions")

Data ={}
Data_points = []

#for loop and assuming max 20 commits in a day
for i in range(1,20):
    listElem = driver.find_elements_by_xpath("//*[@data-count="+ str(i)+ "]")
    for elem in listElem:
        '''print elem.text
        print elem.get_attribute("data-date")
        print elem.get_attribute("data-count")'''
        Data['data-date'] = str(elem.get_attribute("data-date"))
        Data['data-count'] = str(elem.get_attribute("data-count"))
        Data_points.append(Data)

#DataStructure dataPoints:
# X axis = data-date
# Y axis = data-count
print("Final data set:",Data_points)

#Here actual code goes for plotting


driver.close()