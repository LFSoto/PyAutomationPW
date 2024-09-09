import asyncio
from pages.mainpage import CRAutosMainPage
from pages.searchresultspage import CRAutosSearchResultPage
from playwright.async_api import async_playwright

async def testcheckbox():
    async with async_playwright() as p:
        # Crear la instancia del chrome
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Definicion de locators
        main_page = CRAutosMainPage(page)
        result_page = CRAutosSearchResultPage(page)

        # Ir al URL
        await page.goto("https://crautos.com/autosusados/")

        # Hacer click en "split mode"
        await main_page.click_split_mode()
        await page.wait_for_timeout(5000)

        # Hacer click en buscar
        await main_page.click_search_button()

        # Verificar que la pagina fue dividida
        await result_page.is_split_container()

        # await expect(main_page.split_mode).to_be_checked()


asyncio.run(testcheckbox())