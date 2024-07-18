import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.sandbox_page import SandboxPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Type of browser: chrome, firefox, edge, safari"
        )
    # Acá en la lista deben ir las opciones soportadas por la máquina donde va a correr el código

@pytest.fixture(scope="session")
def browser(request):
    browser_type = request.config.getoption("--browser").lower()
    if browser_type == "chrome":
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--headless")  # Ejecuta Chrome en modo sin cabeza
        # chrome_options.add_argument("--disable-gpu")  # Deshabilita la GPU
        chrome_options.add_argument("--no-sandbox")  # Deshabilita el sandbox
        chrome_options.add_argument("--disable-dev-shm-usage")  # Soluciona posibles problemas de memoria compartida en Docker
        chrome_options.add_argument("--remote-debugging-port=9222")  # Habilita el puerto de depuración remota
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
    elif browser_type == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    
    elif browser_type == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        
    elif browser_type == "safari":
        driver = webdriver.Safari() 
    
    else:
        raise ValueError(f"Browser {browser_type} not supported.")
        
    yield driver
    driver.quit()
    
    
@pytest.fixture
def sandbox_page(browser):
    return SandboxPage(browser)