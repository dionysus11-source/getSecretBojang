from selenium import webdriver
import sys
url = "https://www.google.com/search?q=%ED%86%A0%EB%A0%8C%ED%8A%B8%EC%94%A8"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("headless")
driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver',options=options)
driver.get(url)
driver.implicitly_wait(time_to_wait=5)

torrentqq_url = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')

keyword = '놀면'
if sys.argv[1] is not None:
    keyword = sys.argv[1]
query = torrentqq_url.text + '/search/index?keywords='+keyword
driver.get(query)
driver.implicitly_wait(time_to_wait=5)

latest_link = driver.find_elements_by_class_name('tit')

latest_link = driver.find_elements_by_class_name('tit > a')
#latest_link = driver.find_elements_by_tag_name('a')

driver.implicitly_wait(time_to_wait=5)
driver.get(latest_link[0].get_attribute('href'))



file_download_link = driver.find_element_by_class_name('bbs_btn1').get_attribute('href')


print(file_download_link)


driver.close()

# %%

