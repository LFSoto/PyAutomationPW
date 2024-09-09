class CRAutosMainPage:
    def __init__(self, page):
        self.page = page
        self.search_input = "input[name='modelstr']"
        self.search_button = "button[type='submit']"
        self.brand_select = "select[name='brand']"
        self.province_select = "select[name='province']"
        self.split_mode = "input[name='splitmode']"

    async def enter_search_text(self, search_txt):
        await self.page.fill(self.search_input, search_txt)
    
    async def click_search_button(self):
        await self.page.click(self.search_button)

    async def select_brand(self, brand_txt):
        await self.page.select_option(self.brand_select, label=brand_txt)

    async def select_province(self, province_txt):
        await self.page.select_option(self.province_select, label=province_txt)

    async def click_split_mode(self):
        await self.page.click(self.split_mode)