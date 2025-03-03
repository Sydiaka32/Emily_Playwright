import allure
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage


def test_creation_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture

    # Initialize page objects
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation_page = NavigationPage(page)

    with allure.step("Step 1: Navigate to 'New Auction' page"):
        my_auctions_page.navigate_to_new_auction()
        allure.attach(page.screenshot(), name="New Auction Page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 2: Fill in all required fields"):
        with allure.step("Select organiser"):
            auction_page.select_organiser()
            allure.attach(page.screenshot(), name="Organiser Selected", attachment_type=allure.attachment_type.PNG)

        with allure.step("Select procedure"):
            auction_page.select_procedure()
            allure.attach(page.screenshot(), name="Procedure Selected", attachment_type=allure.attachment_type.PNG)

        with allure.step("Extra step: Wait and close Telegram popup"):
            navigation_page.close_telegram_popup()
            allure.attach(page.screenshot(), name="Telegram Popup Closed", attachment_type=allure.attachment_type.PNG)

        with allure.step("Fill in Basic info block"):
            auction_page.fill_basic_info_block()
            allure.attach(page.screenshot(), name="Basic Info Filled", attachment_type=allure.attachment_type.PNG)

        with allure.step("Fill in Details block"):
            auction_page.fill_detail_lot_description_block()
            allure.attach(page.screenshot(), name="Details Block Filled", attachment_type=allure.attachment_type.PNG)

        with allure.step("Fill in Lot info block"):
            auction_page.select_classifier()
            auction_page.fill_lot_info_block()
            auction_page.point_map()
            allure.attach(page.screenshot(), name="Lot Info Block Completed", attachment_type=allure.attachment_type.PNG)

        with allure.step("Wait for 4 seconds"):
            page.wait_for_timeout(4000)

        with allure.step("Upload document"):
            auction_page.upload_document()
            allure.attach(page.screenshot(), name="Document Uploaded", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 3: Save draft"):
        auction_page.save_draft()
        page.wait_for_timeout(3000)
        allure.attach(page.screenshot(), name="Draft Saved", attachment_type=allure.attachment_type.PNG)

    with allure.step("Step 4: Compare data with expected values"):
        card_title = my_auctions_page.get_card_title()
        card_procedure = my_auctions_page.get_card_procedure()
        card_status = my_auctions_page.get_card_status()

        # Attach the retrieved card details for further debugging
        allure.attach(
            f"Title: {card_title}\nProcedure: {card_procedure}\nStatus: {card_status}",
            name="Card Details",
            attachment_type=allure.attachment_type.TEXT
        )

        assert card_title == "Auction", (
            f"Expected title to be 'Auction', but got '{card_title}'"
        )
        assert card_procedure == "Продаж на англійському аукціоні", (
            f"Expected procedure to be 'Продаж на англійському аукціоні', but got '{card_procedure}'"
        )
        assert card_status == "Чернетка", (
            f"Expected status to be 'Чернетка', but got '{card_status}'"
        )
