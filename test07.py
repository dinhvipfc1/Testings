
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
test_driver.find_element(By.XPATH, '//*[@id="register"]/div[1]/input').send_keys('dinh48070@donga.edu.vn')

# Step 5: Nhập Họ
test_driver.find_element(By.XPATH, '//*[@id="register"]/div[2]/input').send_keys('Võ')

# Step 6: Nhập Tên Đệm và Tên
test_driver.find_element(By.XPATH, '//*[@id="register"]/div[3]/input').send_keys('Di Đình')

# Step 7: Nhập Pass
test_driver.find_element(By.XPATH, '//*[@id="register"]/div[4]/input').send_keys('Didinh200111!')

# Step 8: Nhập lại Pass
test_driver.find_element(By.XPATH, '//*[@id="register"]/div[5]/input').send_keys('Didinh200111!')

# Step 9: Bấm vào button "Đăng kí / Register "
button = test_driver.find_element(By.XPATH, '//*[@id="btn-signup"]')
test_driver.execute_script("arguments[0].click();", button)


#tắt testcase
# test_driver.close()
# test_driver.quit()

