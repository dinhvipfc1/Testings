
from selenium import webdriver
from selenium.webdriver.common.by import By
test_driver = webdriver.Chrome()

# Di chuyển đến địa chỉ "....."
test_driver.get('https://vinpearl.com/vi')
          #chờ ngầm định
# 2: Bấm vào button "Đăng nhập"
button = test_driver.find_element(By.XPATH, '//*[@id="block-userblockloginlogout"]/div/li/div/div[1]/a')
test_driver.execute_script("arguments[0].click();", button)
# 3: Bấm vào button "Đăng nhập/ Login"

test_driver.find_element(By.XPATH, '//*[@id="btn-login"]').click()