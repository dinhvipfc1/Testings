from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('https://vinpearl.com/vi')


#Step 2: Bấm vào button "Đăng nhập"
test_driver.find_element(By.XPATH, '//*[@id="block-userblockloginlogout"]/div/li/div/div[1]/a').click()

test_driver.implicitly_wait(4)

# Step 3: Nhập username
test_driver.find_element(By.XPATH, '//*[@id="login"]/div[1]/input').send_keys('didinh200111@gmail.com')


# Step 4: Nhập password
test_driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/input').send_keys('Dinh0208!00')

# Step 5: Bấm vào button "Đăng nhập/Login"
test_driver.find_element(By.XPATH, '//*[@id="btn-login"]').click()


#tắt testcase
# test_driver.close()
# test_driver.quit()