import unittest
from datetime import date, timedelta
from unittest.mock import patch, Mock, ANY
from habitat.data_ingestion.eso_data_downloader import EsoDownloader

class TestEsoDownloader(unittest.TestCase):

    @patch('requests.get')
    def test_download_success(self, mock_get):
        # Mock response data
        response_data = {
            "result": {
                "records": [
                    {"name": "John", "age": 30},
                    {"name": "Jane", "age": 25}
                ]
            }
        }

        # Set up the mock response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = response_data

        # Set the mock response for the requests.get method
        mock_get.return_value = mock_response

        # Create an instance of the downloader
        downloader = EsoDownloader()

        # Perform the download
        result = downloader.download()

        # Assert that the result matches the expected records
        expected_records = response_data["result"]["records"]
        self.assertEqual(result, expected_records)

        # Assert that requests.get was called with the correct URL and params
        expected_url = 'https://api.nationalgrideso.com/api/3/action/datastore_search_sql'
        mock_get.assert_called_with(expected_url, params=ANY)

    def test_date_iso_today(self):
        # Create an instance of the downloader
        downloader = EsoDownloader()

        # Get the ISO format of today's date
        today_iso = date.today().isoformat() + "T00:00:00Z"

        # Check if the returned value matches the expected ISO format
        self.assertEqual(downloader.date_iso_today(), today_iso)

    def test_date_iso_yesterday(self):
        # Create an instance of the downloader
        downloader = EsoDownloader()

        # Calculate yesterday's date
        yesterday = date.today() - timedelta(days=1)

        # Get the ISO format of yesterday's date
        yesterday_iso = yesterday.isoformat() + "T00:00:00Z"

        # Check if the returned value matches the expected ISO format
        self.assertEqual(downloader.date_iso_yesterday(), yesterday_iso)

if __name__ == '__main__':
    unittest.main()
