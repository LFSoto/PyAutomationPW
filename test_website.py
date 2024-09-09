import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Prueba de búsqueda en Google
        await page.goto("https://www.google.com")
        await page.fill("textarea[title='Buscar']", "Automation with Playwright")
        await page.press("input[value='Buscar con Google']", "Enter")

        # Esperar a que los resultados se carguen
        await page.wait_for_selector("#rso")

        # Verificar que los resultados contienen la búsqueda esperada
        results = await page.inner_text("body")
        assert "Playwright" in results
        print('\033[92m'+"Búsqueda en Google exitosa"+'\033[92m')

        await browser.close()

asyncio.run(main())