from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')

# Khởi tạo trình duyệt và mở trang web
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/groups/968778250642512/posts/1555700318616966/")

# Chờ trang web load xong
driver.implicitly_wait(50)

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Tìm tất cả các thẻ div và lặp qua từng thẻ để in ra nội dung text
divs = soup.find_all('div')

for idx, div in enumerate(divs, start=1):
    text_content = div.text.strip()  # Sử dụng strip để loại bỏ khoảng trắng thừa
    div_class = div.get('class')
    # if text_content == "":
    #     continue
    # print(f"Div {idx} - Text Content: {text_content}")
    # print(f"Div {idx} - Class: {div_class}")
    # print("\n")

    if not div_class:
        continue  # Bỏ qua nếu không có class

        # Tạo CSS Selector với các class của phần tử div
    css_selector = '.' + '.'.join(div_class)

    # Sử dụng CSS Selector để trực tiếp truy xuất và lấy text
    text_content = soup.select_one(css_selector).text.strip() if soup.select_one(css_selector) else ""

    if text_content:
        print(f"Div {idx} - Text Content: {text_content}")
        print(f"Div {idx} - Class: {div_class}")
        print("\n")

# Nếu không có thẻ div nào, in ra thông báo
if not divs:
    print("Không tìm thấy thẻ div.")


div_class = ['x9f619', 'x1n2onr6', 'x1ja2u2z', 'x2bj2ny', 'x1qpq9i9', 'xdney7k', 'xu5ydu1', 'xt3gfkd', 'xh8yej3', 'x6ikm8r', 'x10wlt62', 'xquyuld']
css_selector = '.' + '.'.join(div_class)

# Sử dụng CSS Selector để trực tiếp truy xuất và lấy text
text_content = soup.select_one(css_selector).text.strip() if soup.select_one(css_selector) else ""
print(f"Text Bài Viết: {text_content} \n")

# Class cần trích xuất
div_class = ['x1n2onr6', 'x1swvt13', 'x1iorvi4', 'x78zum5', 'x1q0g3np', 'x1a2a7pz']
css_selector = '.' + '.'.join(div_class)

# Sử dụng CSS Selector để trực tiếp truy xuất và lấy text
elements_with_class = soup.select(css_selector)

# Lặp qua từng phần tử và in ra nội dung
for idx, element in enumerate(elements_with_class, start=1):
    text_content = element.text.strip()

    if text_content:
        print(f"Element {idx} - Text Comment: {text_content}")
        print("\n")

time.sleep(1)
driver.quit()