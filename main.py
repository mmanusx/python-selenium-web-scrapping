# Selenium (Webdriver) Kütüphanesi
# Browser gibi davranır bs dan daha gelişmiştir.
# Selenium kullanımı için, chrome versiyonuna bakılır
# Chrom versiyonuna göre, chrome driverı indirilir(https://chromedriver.chromium.org/downloads)
# Driver sürekli kullanılacak bir lokastona taşınır
#import selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/hudayis/Documents/Development/chromedriver.exe"


#driver = webdriver.Chrome(executable_path=chrome_driver_path) #  DeprecationWarning: aldım
ser = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=ser)

# beautiful sadece html olan siteler için çok kullanışlı ancak js, angular vb ile render edilmiş siteler için selenium daha kullanışlı

# doc için selenium with python diye aratmak gerek https://selenium-python.readthedocs.io/
############ Sayfayı Açma #############
# mac bağlanmana izin vermeyecek // system-> security & privacy // allow anyway
driver.get("https://www.amazon.com/dp/B08GC6PL3D/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0")
# price = driver.find_element(By.CSS_SELECTOR, ".a-span12 .a-offscreen") # selenium element olarak döndü
# bulamazsa xpath kesin çözüm https://www.w3schools.com/xml/xpath_intro.asp
price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
print(price.text)





########### Kapatma #################
#driver.close() # açılan chrome pencerisini(aktif tab) yüklendikten sonra kapatır
driver.quit() # tarayıcıyı kapatır