
from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "....."
test_driver.get('https://vinpearl.com/vi')


#Step 2: Bấm vào button "Đăng nhập"
test_driver.find_element(By.XPATH, '//*[@id="block-userblockloginlogout"]/div/li/div/div[1]/a').click()

test_driver.implicitly_wait(4)
#Step 3: Bấm vào button "Đăng kí"
test_driver.find_element(By.XPATH, '//*[@id="vpt-main-login"]/div[2]/div/div[2]/ul/li[2]/a/span').click()


# Step 4: Nhập email
test_driver.find_element(By.XPATH, '//*[@id="register"]/div[1]/input').send_keys('didinh200111@gmail.com')

# Step 5: Bấm vào button "Đăng kí / Register "
# test_driver.find_element(By.XPATH, '//*[@id="btn-signup"]').click()
button = test_driver.find_element(By.XPATH, '//*[@id="btn-signup"]')
test_driver.execute_script("arguments[0].click();", button)


#tắt testcase
# test_driver.close()
# test_driver.quit()

