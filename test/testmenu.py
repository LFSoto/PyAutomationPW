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
        await page.goto("https://crautos.com/")

        # Verificar el titulo
        result = await page.inner_text("body")
        assert "Encuentra el auto que quieres" in result

asyncio.run(main())