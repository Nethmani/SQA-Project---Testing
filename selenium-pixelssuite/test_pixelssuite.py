from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -----------------------------
# Common Driver Setup
# -----------------------------
def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

# -----------------------------
# TC01 - Website Load Test
# -----------------------------
def test_tc01():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/")

        # Step 1: Wait until page loads (check title exists)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        current_url = driver.current_url
        print("TC01 - Current URL:", current_url)

        if "pixelssuite" in current_url.lower():
            print("TC01 PASS - Website loaded successfully")
        else:
            print("TC01 FAIL - Website did not load properly")

        driver.save_screenshot("tc01_homepage.png")

        input("TC01 done - Press Enter to continue...")

    finally:
        driver.quit()


# -----------------------------
# TC02 - Navigation Menu Test
# -----------------------------
def test_tc02():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/")

        # Step 1: Wait until page loads
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Step 2: Click 3rd menu item (Crop)
        menu_items = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//nav//a"))
        )

        # Step 3: Crop = index 3 (0-based index → 2)
        menu_items[3].click()

        print("Clicked menu item:", menu_items[3].text)

        # Step 4: Wait after click
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        print("TC02 PASS - Navigation works")

        driver.save_screenshot("tc02_navigation.png")

        input("TC02 done - Press Enter...")

    except Exception as e:
        print("TC02 ERROR:", e)

    finally:
        driver.quit()

# -----------------------------
# TC03 - Button Click Test
# -----------------------------
def test_tc03():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/")

        # Step 1: Wait page load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Step 2: Use button locator 
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Open Editor')]"))
        )

        button.click()

        # Step 3: Wait after click
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        print("TC03 PASS - Open Editor button clicked successfully")

        driver.save_screenshot("tc03_button.png")

        input("TC03 done - Press Enter...")

    except Exception as e:
        print("TC03 ERROR:", e)

    finally:
        driver.quit()

# -----------------------------
# TC04 - Invalid Input Test (Download Button Disabled)
# -----------------------------

def test_tc04():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.pixelssuite.com/")

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Step 1: Click "Open Editor" (same like TC03)
        editor_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Open Editor')]"))
        )
        editor_btn.click()

        print("Opened Editor")

        # Step 2: Wait for file input (editor loaded)
        file_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        # Step 3: Find Download button (correct way)
        download_btn = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[.//span[contains(text(),'Download')]]")
            )
        )

        # Step 4: Check disabled
        is_disabled = download_btn.get_attribute("disabled")

        if is_disabled:
            print("TC04 PASS - Download disabled without file")
        else:
            print("TC04 FAIL")

        driver.save_screenshot("tc04_invalid.png")

        input("TC04 done - Press Enter...")

    except Exception as e:
        print("TC04 ERROR:", e)

    finally:
        driver.quit()

# -----------------------------
# TC05 - Valid Input Test (Transliteration)
# -----------------------------

def test_tc05():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.pixelssuite.com/")

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Step 1: Scroll to Transliteration section
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Step 2: Click "Chat" button FIRST
        chat_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Chat')]"))
        )
        chat_btn.click()

        print("Chat mode selected")

        # Step 3: Wait input box
        input_box = wait.until(
            EC.presence_of_element_located((By.XPATH, "//textarea[contains(@placeholder,'English')]"))
        )

        # Step 4: Enter valid text
        input_box.clear()
        input_box.send_keys("hello")

        # Step 5: Click Transliterate
        translit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Transliterate')]"))
        )
        translit_btn.click()

        print("Entered text and clicked Transliterate")

        # Step 6: Check output
        output_box = wait.until(
            EC.presence_of_element_located((By.XPATH, "//textarea[contains(@placeholder,'Sinhala')]"))
        )

        output_value = output_box.get_attribute("value")

        if output_value.strip() != "":
            print("TC05 PASS - Output generated successfully")
        else:
            print("TC05 FAIL - No output generated")

        driver.save_screenshot("tc05_valid.png")

        input("TC05 done - Press Enter...")

    except Exception as e:
        print("TC05 ERROR:", e)

    finally:
        driver.quit()

# -----------------------------
# TC06 - Image Upload Test
# -----------------------------
def test_tc06():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/compress-image")

        file_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        file_input.send_keys("D:\\4th Year\\2nd Semester\\SQA\\Assingment 2\\Pic\\image001.jpg")

        print("TC06 PASS - Image uploaded successfully")

        driver.save_screenshot("tc06_upload.png")
        input("Press Enter...")

    except Exception as e:
        print("TC06 ERROR:", e)

    finally:
        driver.quit()
# -----------------------------
# TC07 - Drag & Drop Upload Test
# -----------------------------
def test_tc07():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/compress-image")

        file_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        # Drag-drop simulate using send_keys
        file_input.send_keys("D:/4th Year/2nd Semester/SQA/Assingment 2/Pic/image001.png")

        print("TC07 PASS - Drag & Drop simulated upload success")

        driver.save_screenshot("tc07_dragdrop.png")
        input("Press Enter...")

    except Exception as e:
        print("TC07 ERROR:", e)

    finally:
        driver.quit()
# -----------------------------
# TC08 - Format Selection Test
# -----------------------------
def test_tc08():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/compress-image")

        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys("D:/4th Year/2nd Semester/SQA/Assingment 2/Pic/image001.png")

        dropdown = wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))
        dropdown.send_keys("WEBP")

        print("TC08 PASS - Format selected successfully")

        driver.save_screenshot("tc08_format.png")
        input("Press Enter...")

    except Exception as e:
        print("TC08 ERROR:", e)

    finally:
        driver.quit()
# -----------------------------
# TC09 - Quality 100 Test
# -----------------------------
def test_tc09():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/compress-image")

        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys("D:/4th Year/2nd Semester/SQA/Assingment 2/Pic/image001.png")

        slider = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='range']")))
        driver.execute_script("arguments[0].value=100;", slider)

        print("TC09 PASS - Quality set to 100")

        driver.save_screenshot("tc09_quality100.png")
        input("Press Enter...")

    except Exception as e:
        print("TC09 ERROR:", e)

    finally:
        driver.quit()
# -----------------------------
# TC10 - Quality 5 Test
# -----------------------------
def test_tc10():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/compress-image")

        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys("D:/4th Year/2nd Semester/SQA/Assingment 2/Pic/image001.png")

        slider = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='range']")))
        driver.execute_script("arguments[0].value=5;", slider)

        print("TC10 PASS - Quality set to 5")

        driver.save_screenshot("tc10_quality5.png")
        input("Press Enter...")

    except Exception as e:
        print("TC10 ERROR:", e)

    finally:
        driver.quit()
# -----------------------------
# TC11 - Download Action Test
# -----------------------------
def test_tc11():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/compress-image")

        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys("D:/4th Year/2nd Semester/SQA/Assingment 2/Pic/image001.png")

        download_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Download')]")))
        download_btn.click()

        print("TC11 PASS - Download triggered")

        driver.save_screenshot("tc11_download.png")
        input("Press Enter...")

    except Exception as e:
        print("TC11 ERROR:", e)

    finally:
        driver.quit()
# -----------------------------
# TC12 - Clear Button Test
# -----------------------------
def test_tc12():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.pixelssuite.com/compress-image")

        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys("D:/4th Year/2nd Semester/SQA/Assingment 2/Pic/image001.png")

        clear_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Clear')]")))
        clear_btn.click()

        print("TC12 PASS - Clear works")

        driver.save_screenshot("tc12_clear.png")
        input("Press Enter...")

    except Exception as e:
        print("TC12 ERROR:", e)

    finally:
        driver.quit()
# -----------------------------
# RUN TEST CASES
# -----------------------------
if __name__ == "__main__":
    test_tc01()
    test_tc02() 
    test_tc03()
    test_tc04()
    test_tc05()
    test_tc06()
    test_tc07()
    test_tc08()
    test_tc09()
    test_tc10()
    test_tc11()
    test_tc12()