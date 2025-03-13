def test_creation_draft(create_draft_auction):
    """Test that a draft auction is created successfully."""
    auction_data = create_draft_auction

    assert auction_data["title"] == "Auction", \
        f"Expected title to be 'Auction', but got '{auction_data['title']}'"
    assert auction_data["procedure"] == 'Продаж на "англійському аукціоні"', \
        f"Expected procedure to be 'Продаж на англійському аукціоні', but got '{auction_data['procedure']}'"
    assert auction_data["status"] == "Чернетка", \
        f"Expected status to be 'Чернетка', but got '{auction_data['status']}'"