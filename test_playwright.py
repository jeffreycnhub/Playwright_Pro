import  pytest
from playwright.sync_api import sync_playwright

# 使用 pytest-fixture 获取 Playwright 实例
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # 启动 Chromium 浏览器
        browser = p.chromium.launch(headless=False)  # 设置 headless=False 来查看浏览器
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    # 创建一个新的浏览器页面
    page = browser.new_page()
    yield page
    page.close()

# 编写一个测试
def test_qq_com_title(page):
    page.goto("https://www.qq.com")
    #截取页面的屏幕截图，并且保存
    page.screenshot(path="qq.png")
    title = page.title()
    assert title == "腾讯网"
