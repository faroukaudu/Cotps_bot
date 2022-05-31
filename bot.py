from selenium import webdriver
import time
from csv import DictReader
import pandas as pd
data = pd.read_csv('user2.csv')


count = 0
memeber_num = len(data)
web = webdriver.Chrome()

#Visit this below webiste


def firstLauch():
    global count
    global web
    time.sleep(3)
    web.get('https://www.cotps.com/#/pages/login/login?originSource=transaction')

    count = 0

    #Launch Browser

    #Wait for 6 sec
    time.sleep(10)

    tracking_usercount()


#countryCode = "1"
#code = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-input/div/input')
#code.send_keys(countryCode)
def transaction_hall():
    #Pop up
    time.sleep(3)
    try:
        popUps = web.find_element_by_xpath('/html/body/uni-app/uni-modal/div[2]/div[3]/div')
        popUps.click()
        time.sleep(3)
        tranHall = web.find_element_by_xpath('/html/body/uni-app/uni-tabbar/div[1]/div[3]/div')
        tranHall.click()
        time.sleep(7)
        trade_loop()
    except:
        time.sleep(3)
        tranHall = web.find_element_by_xpath('/html/body/uni-app/uni-tabbar/div[1]/div[3]/div')
        tranHall.click()
        time.sleep(7)
        trade_loop()






        #checking if element is displayed
        #popUplogin = web.find_element_by_xpath("/html/body/uni-app/uni-modal/div[2]/div[3]/div").is_displayed();
        #CLOSE THE POPUP
        #popUpClose = web.find_element_by_xpath('/html/body/uni-app/uni-modal/div[2]/div[3]/div')
        #NAVIGATING TO TRANSACTION HALL







    # #CLOSE THE POPUP
    # popUpClose = web.find_element_by_xpath('/html/body/uni-app/uni-modal/div[2]/div[3]/div')
    # popUpClose.click()
    # time.sleep(2)
    #
    #
    #
    # #NAVIGATING TO TRANSACTION HALL
    # tranHall = web.find_element_by_xpath('/html/body/uni-app/uni-tabbar/div[1]/div[3]/div')
    # tranHall.click()
    # time.sleep(6)
    # 'trade_loop()'
    # login_out()
    #tesing purposes




def login_users(cc, pho, pas):
    global count
    print("count b4", count)
    count +=1
    print("count AFTER", count)

    #CLICKING ON COUNTRY CODE INVISIBLE BUTTON
    time.sleep(2)
    countryCode = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-text')
    countryCode.click()
    #WAITING ONE SEC FOR MODAL BOX TO LOAD
    time.sleep(3)
    #INSERTING COUNTRY CODE
    countryCI = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-input/div/input')
    countryCI.send_keys(cc)
    #COMFIRMING COUNTRY CODE
    time.sleep(3)

    confirmCC = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-button')
    confirmCC.click()
    #INPUTING PHONE NUMBER & PASSWORD

    #myPass = "4474.a44"
    num = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input')
    password = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input')
    num.send_keys(pho)
    password.send_keys(pas)
    time.sleep(3)
    #LOGGING INTO YOUR ACCOUNT
    logIN = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-button')
    logIN.click()

    #WAITING FOR PAGE TO LOAD
    time.sleep(8)

    transaction_hall()

def trade_loop():
    #DIVISIONNUM
    divisioNum = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]')
    total = int(float(divisioNum.text))
    while total >= 5:
        print('selling again')
        #LOOKING FOR A SELL ORDER.
        checkOder = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button')
        checkOder.click()
        time.sleep(9)

        #LOOKING FOR A SELL ORDER.
        selling = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]')
        selling.click()
        time.sleep(9)

        #Closing selling session.
        soldClose = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button')
        soldClose.click()
        time.sleep(9)

        divisioNum = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]')
        total = int(float(divisioNum.text))
    time.sleep(6)
    login_out()







    print(total)

def login_out():
    #Navigate to Mine Menu
    time.sleep(2)
    minning = web.find_element_by_xpath('/html/body/uni-app/uni-tabbar/div[1]/div[5]/div')
    minning.click()
    time.sleep(7)

    #Scrolling down to find logout button element

    web.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

    #Logging Out of account
    logOutsite = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-button')
    logOutsite.click()
    time.sleep(3)
    #web.close()
    tracking_usercount()



    #CLosing pop up to Mine Menu
    #comfirmLogout_popup = web.find_element_by_xpath('/html/body/uni-app/uni-modal/div[2]/div[3]/div')
    #comfirmLogout_popup.click()
    #time.sleep(3)





def tracking_usercount():
    global count
    global memeber_num
    global web

    if count <= memeber_num-1:
        print(data["Name"][count])
        print(memeber_num)
        print("its here ALOOOOONNE!!!")
        login_users(str(data["Country_code"][count]), str(data["Phone_num"][count]), data["Password"][count])
        print("REACHING HERE!!!!!!")

        #print('login in '+ users[count]['name'] +' Now!')
        #login_users('234', '8160278321', '4474.a44')
        #login_users(users[count]['mycountry'],users[count]['phone'],users[count]['pass'])

    else:
        print("Stop!!!!!!!!!!!!!!!")
        #7980 sec
        count = 0
        time.sleep(3)
        web.close()
        #Time it would take for the next sequence to run.
        '''time.sleep(30)
        print('30 Seconds to next Executions')
        TESTING TIME'''
        time.sleep(20)
        '''print('10 Seconds to next Executions')
        time.sleep(10)'''
        #REAL CODE

        # time.sleep(3600)
        # print('1 hour,13 Min before next Execution')
        # time.sleep(3600)
        # print('13 Min before next Execution')
        # time.sleep(600)
        # print('(Three)3 Min before next Execution')
        # time.sleep(150)
        # print('Starting now.')



        print('Starting next Executions')

        web = webdriver.Chrome()
        time.sleep(3)
        firstLauch()


        'Reset count to 1'
        'close browser'
        'wait for two hours'
        'open browser to the url'
        'Call login users and pass in variables'



firstLauch()

'''
#LOOKING FOR A SELL ORDER.
def orderChecker():
    checkOder = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button')
    checkOder.click()
    time.sleep(8)




    #LOOKING FOR A SELL ORDER.
    selling = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]')
    selling.click()
    time.sleep(8)

    soldClose = web.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button')
    soldClose.click()
    '''
