from playwright.async_api import APIRequestContext


class ApiRequests:
    def __init__(self, api_context: APIRequestContext):
        self.api_context = api_context

    async def get_latest_auction_id(self) -> str:
        # Data payload for the POST request (adjust if needed)
        data = {
            # Add any required payload parameters here
        }

        # Perform the POST request
        response = await self.api_context.post("", data=data)
        assert response.ok, f"Failed to fetch auctions: {response.status}"

        # Parse the JSON response
        json_data = await response.json()
        if not json_data or not isinstance(json_data, list):
            raise ValueError("Unexpected response format or no auctions found.")

        # Extract the first auction ID
        auction_id = json_data[0].get("id")
        if not auction_id:
            raise ValueError("No auction ID found in the response.")

        return auction_id
