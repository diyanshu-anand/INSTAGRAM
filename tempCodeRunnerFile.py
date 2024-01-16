
# driver = webdriver.Chrome()

# #open the webpage
# driver.get("http://www.instagram.com")

# #target username
# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# #enter username and password
# username.clear()
# username.send_keys("divya_grd")
# password.clear()
# password.send_keys("divya_131203")

# #target the login button and click it
# button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


# alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
# alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
# searchbox.clear()

# keyword = input("Enter the Instagram Id");
# time.sleep(30)
# searchbox.send_keys(keyword)
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)
# #scroll
# driver.execute_script("window.scrollTo(0, 4000);")
# #select images
# images = driver.find_elements_by_tag_name('img')
# images = [image.get_attribute('src') for image in images]
# images = images[:-2] #slicing-off IG logo and Profile picture
# print('Number of scraped images: ', len(images))