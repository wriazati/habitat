import requests

from .abstract_data_downloader import AbstractDownloader
from datetime import date, timedelta


class EsoDownloader(AbstractDownloader):

    def download(self):

        # TODO: Dependencies should be injected
        resource_target = "6fd8e042-be27-4c67-ad59-5acdd2a7b0fd"
        member_name = "HABITAT ENERGY LIMITED"
        order_entry_time = self.date_iso_yesterday()
        limit = 100

        query = f'''SELECT COUNT(*) OVER () AS _count, * FROM "{resource_target}" WHERE "MemberName" = '{member_name}' AND "OrderEntryTime" >= '{order_entry_time}' ORDER BY "_id" ASC LIMIT {limit}'''
        params = {'sql': query}
        data = None

        try:
            response = requests.get('https://api.nationalgrideso.com/api/3/action/datastore_search_sql', params=params)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            data = response.json()["result"]
        except requests.exceptions.RequestException as e:
            print(e)

        return data['records']

    def date_iso_today(self) -> str:
        return date.today().isoformat() + "T00:00:00Z"

    def date_iso_yesterday(self) -> str:
        yesterday = date.today() - timedelta(days=1)
        return yesterday.isoformat() + "T00:00:00Z"
