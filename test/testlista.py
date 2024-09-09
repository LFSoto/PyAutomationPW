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

        # Ir al URL
        await page.goto("https://crautos.com/autosusados/")

        elements = await page.query_selector_all(".container .modeltitle b")
        
        # Extraer los textos de los primeros 10 resultados
        texts = []
        for i in range(min(10, len(elements))): 
            text = await elements[i].inner_text()
            texts.append(text)

        # Convierte los textos a enteros
        values = [int(text) for text in texts]

        # Calcula el promedio
        average = sum(values) / len(values) if values else 0

        print(f"Los primeros 10 años de los vehículos son: {values}")
        print(f"El promedio de los primeros 10 años de los vehículos es: {average}")
        await browser.close()
asyncio.run(main())