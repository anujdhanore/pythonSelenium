from behave import given, when, then

@given(u'Open web shop')
def step_impl(context):

    global  driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #options.add_argument('--headless')
    s = Service("C:\\Users\\anuj.dhanore_infobea\\Downloads\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
