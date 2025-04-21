import os
import requests
import pandas as pd
from geopy.distance import geodesic
from llama_index.experimental import PandasQueryEngine


class CoffeeScraper:
    def __init__(self):
        self.api_token = os.getenv("SCRAPELESS_API_TOKEN")
        self.gallery_coords = (45.4299, -75.6939)  # National Gallery of Canada location
        self.df = pd.DataFrame(columns=[
            "name", "address", "price_level",
            "rating", "distance_km", "scraped_at"
        ])

    def _send_scrapeless_request(self, query: str):
        host = "api.scrapeless.com"
        url = f"https://{host}/api/v1/scraper/request"

        payload = {
            "actor": "scraper.google.maps",
            "input": {
                "q": query,
                "engine": "google_maps",
                "type": "search",
                "ll": "@45.4299,-75.6939,14z",
                "google_domain": "google.com",
                "gl": "ca",
                "hl": "en-sg",
                "data": "",
                "place_id": "",
                "start": ""
            }
        }

        response = requests.post(
            url,
            headers={"x-api-token": self.api_token},
            json=payload
        )

        if response.status_code == 200:
            res_data = response.json()
            print(f"Scraping status: {res_data}")
            return res_data["local_results"]
        else:
            raise Exception(f"Scraping failed: {response.text}")

    def scrape_nearby_coffee(self):
        try:
            results = self._send_scrapeless_request("coffee")

            for place in results:
                shop_coords = (place["gps_coordinates"]["latitude"], place["gps_coordinates"]["longitude"])
                print(f"shop_coords: {shop_coords}")
                print(f"distance: {round(geodesic(self.gallery_coords, shop_coords).km, 2)}")
                self.df = pd.concat([self.df, pd.DataFrame([{
                    "name": place["title"],
                    "address": place["address"],
                    "price_level": len(place.get("price", "")),
                    "rating": place.get("rating", None),
                    "distance_km": round(geodesic(self.gallery_coords, shop_coords).km, 2),
                    "scraped_at": pd.Timestamp.now()
                }])], ignore_index=True)

            print(f"Successfully scraped data for {len(results)} coffee shops.")
        except Exception as e:
            print(f"The scraping failed.: {str(e)}")

    def get_query_engine(self):
        return PandasQueryEngine(
            df=self.df,
            verbose=True,
            instruction_str=(
                "You are a coffee shop analyst. Use this data to answer questions "
                "about coffee shops near National Gallery of Canada. "
                "Key fields: name, price_level ($1-3), rating (1-5), distance_km."
            )
        )


coffee_scraper = CoffeeScraper()
