class CRAutosSearchResultPage:
    def __init__(self, page):
        self.page = page
        self.car_province_list = "tr:nth-child(5) td:nth-child(4)"
        self.split_container = "body .splitcontainer"

    async def validate_province_list(self, province):
        provinces = await self.page.query_selector_all(self.car_province_list)
        for i in range(min(10, len(provinces))):
            text = await provinces[i].inner_text()
            if text == province:
                print(i,". ", province, " is ", text)

    async def is_split_container(self):
        await self.page.is_visible(self.split_container)
        print('\033[92m'+"Es visible"+'\033[92m')

