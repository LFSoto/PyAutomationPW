import asyncio
from pages.mainpage import CRAutosMainPage
from pages.searchresultspage import CRAutosSearchResultPage
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        # Crear la instancia del chrome
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Crear paginas
        main_page = CRAutosMainPage(page)
        result_page = CRAutosSearchResultPage(page)

        # Ir al URL
        await page.goto("https://crautos.com/autosusados/")

        # Llenar text field con criterio busqueda
        await main_page.enter_search_text("RAV4")

        # Hacer click en buscar
        await main_page.click_search_button()

        # Validacion 
        results = await page.inner_text("body")
        assert "Autos Usados" in results
        await page.wait_for_timeout(5000)
        print('\033[92m'+"Test exitoso"+'\033[92m')

        await browser.close()
        
asyncio.run(main())