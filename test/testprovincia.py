import asyncio
from pages.mainpage import CRAutosMainPage
from pages.searchresultspage import CRAutosSearchResultPage
from playwright.async_api import async_playwright

async def testprovincia():
    async with async_playwright() as p:
        # Instancia Browser - Configuracion inicial
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Definicion de locators
        main_page = CRAutosMainPage(page)
        result_page = CRAutosSearchResultPage(page)

        # Definicion de variables 
        provincia = 'Heredia'

        # Ir al URL
        await page.goto("https://crautos.com/autosusados/")

        # Seleccionar la provincia
        await main_page.select_province(provincia)
        await page.wait_for_timeout(5000)

        # Hacer click en buscar
        await main_page.click_search_button()
        await page.wait_for_timeout(5000)

        # Verificar que los resultados hagan match con la provincia
        await result_page.validate_province_list(provincia)
        


        await browser.close()
        

asyncio.run(testprovincia())