from playwright.async_api import async_playwright

from pages.auction_page import AuctionPage
from pages.login_page import LoginPage
from pages.my_auctions_page import MyAuctionsPage
from pages.navigation_page import NavigationPage
from utils.api_requests import ApiRequests


async def test_create_copy(api_request_context):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        auction_actions = AuctionPage(page)
        my_auctions_page = MyAuctionsPage(page)
        api_requests = ApiRequests(api_request_context)

        login_page = LoginPage(page)
        navigation_page = NavigationPage(page)

        # Ensure login and navigation are awaited correctly
        await login_page.login()
        await navigation_page.navigate_to_my_auctions()

        # Debug: Check if the auction ID is being fetched correctly
        initial_id = await api_requests.get_latest_auction_id()
        assert initial_id, f"Failed to retrieve the initial auction ID: {initial_id}"
        print(f"Initial Auction ID: {initial_id}")

        # Perform actions to create a copy
        await my_auctions_page.publish_copy()
        await my_auctions_page.copy_popup()
        await auction_actions.save_changes()

        # Fetch the final auction ID and check if it’s valid
        final_id = await api_requests.get_latest_auction_id()
        assert final_id, f"Failed to retrieve the final auction ID: {final_id}"
        print(f"Final Auction ID: {final_id}")

        # Verify that the IDs are different
        assert initial_id != final_id, "The auction ID did not change after creating a copy"

        # Clean up
        await browser.close()
