# Playwright_Pro
Playwright 框架的学习和应用
使用的语言：Python

Playwright 是一个由 Microsoft 开发的开源自动化测试框架，用于在浏览器中执行端到端测试。
它支持 Chrome、Firefox 和 WebKit 等浏览器，并提供了强大的 API 来模拟用户交互、抓取页面内容、截图和生成报告等功能。

部分代码说明：
pytest.fixture：这是 pytest 提供的装置（fixtures）功能。我们用它来为每个测试提供必要的资源，比如浏览器实例和页面。
browser fixture 启动一个 Chromium 浏览器实例，并在测试结束后关闭它。
page fixture 为每个测试创建一个新的页面，并在测试结束后关闭该页面。
page.goto()：模拟浏览器导航到指定的 URL。
page.title()：获取页面的标题。
assert：断言标题是否与预期的“Example Domain”匹配。

使用 pytest-playwright 插件的好处
pytest-playwright 插件提供了很多有用的功能，比如自动启动和关闭浏览器实例，以及支持异步模式。

Playwright 测试夹具和资源管理
使用 pytest 的测试夹具，你可以轻松地管理浏览器和页面等资源。以下是几个常用的测试夹具和资源管理功能：
Scope：你可以设置测试夹具的作用域，像 scope="session" 表示整个测试会话中都使用同一个浏览器实例，而 scope="function" 则表示每个测试函数都会使用一个新的浏览器实例。
yield：在测试夹具中，yield 表达式的前后代码分别表示资源的初始化和清理部分，yield 后面的部分会在测试结束后执行。

总结：
通过结合使用 Playwright 和 pytest，你可以创建强大的浏览器自动化测试框架。
pytest 提供了简洁的语法和强大的测试功能，而 Playwright 提供了高效、跨浏览器的自动化能力。
通过合适的测试夹具、断言和资源管理，可以非常轻松地进行浏览器端到端的测试。
