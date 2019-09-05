

# WebScrapping Of All comments of A Reddit Post 


from selenium import webdriver
crome = r"C:\Users\Aarush\Desktop\chromedriver.exe"
driver = webdriver.Chrome(crome)
driver.get("https://www.reddit.com/r/classicalmusic/comments/cw75vr/what_are_you_listening_to_right_now/")

driver.find_element_by_xpath("""//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div[3]/div[1]/div[1]/div[4]/div/button""").click()

posts = driver.find_elements_by_class_name("_1qeIAgB0cPwnLhDF9XSiJM")
for post in posts:
	print(post.text)
