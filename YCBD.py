from selenium import webdriver
import time
import win32clipboard
a=[]
while(True):    
    #GET Clipboard data
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
        print("Error with clipboard")
    if 'youtube' in data:
        if data in a:
            print("Already downloaded")
            continue
        a.append(data)
        print (data)
        baseurl = "http://www.clipconverter.cc/"

        xpaths = { 'mediaurlBox' : "//input[@name='mediaurl']",
                       'passwordTxtBox' : "//input[@name='password']",
                       'submitButton' :   "//input[@name='submiturl']"
                     }
        try:
            NEXT_BUTTON_XPATH = '//input[@class="button ui-button ui-widget ui-state-default ui-corner-all" and @value="Start!"]'
            mydriver = webdriver.Firefox()
            mydriver.get(baseurl)
            mydriver.maximize_window()
            mydriver.find_element_by_xpath(xpaths['mediaurlBox']).send_keys(data)
            mydriver.find_element_by_css_selector('.button.ui-button.ui-widget.ui-state-default.ui-corner-all').click()
            time.sleep(10)
            mydriver.find_element_by_xpath(NEXT_BUTTON_XPATH).click()
            time.sleep(60)
            mydriver.find_element_by_id('downloadbutton').click()
            time.sleep(30)
        except:
            print("Trying again")
