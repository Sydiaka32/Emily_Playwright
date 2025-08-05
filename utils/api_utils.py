import requests
from config.settings import ConfigParser
from datetime import datetime, timedelta, timezone
from pathlib import Path



def api_login_organiser():
    """Logs in and returns the access token."""
    url = f"{ConfigParser.base_url}/auth/api/v1.0/users/login"
    payload = {
        "email": ConfigParser.email_t1,
        "password": ConfigParser.password_user
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        json_data = response.json()
        return json_data.get("accessToken")  # Return the token
    else:
        raise Exception(f"Login failed: {response.status_code}, {response.text}")

def api_login_participant():
    """Logs in and returns the access token."""
    url = f"{ConfigParser.base_url}/auth/api/v1.0/users/login"
    payload = {
        "email": ConfigParser.email_t3,
        "password": ConfigParser.password_user
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        json_data = response.json()
        return json_data.get("accessToken")  # Return the token
    else:
        raise Exception(f"Login failed: {response.status_code}, {response.text}")


def upload_document():
    """Uploads a document for a given auction via API and returns the document ID."""
    token = api_login_organiser()  # Obtain the token by logging in

    # Calculate the repository root directory.
    repo_root = Path(__file__).resolve().parent.parent  # Adjust based on your structure

    # Build the path to the document which should always be in 'utils/attachments/Test_PDF.pdf'
    document_path = repo_root / "utils" / "attachments" / "Test_PDF.pdf"

    if not document_path.exists():
        raise FileNotFoundError(f"Test document missing at: {document_path}")

    # Construct the URL to upload the document
    url = (f"{ConfigParser.base_url}/api/v1.0/auctions/documents"
           f"/upload?documentType=TECHNICAL_SPECIFICATIONS&auctionType=BASIC_SELL_ENGLISH")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Open and upload the file
    with open(document_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, headers=headers, files=files)

    # Check the response
    if response.status_code == 200:
        json_data = response.json()
        document_id = json_data.get("id")
        print(f"Document uploaded successfully. Document ID: {document_id}")
        return document_id
    else:
        raise Exception(f"Failed to upload document: {response.status_code}, {response.text}")


def generate_fast_manual_time():
    """Generates the start time for the auction by adding 32 minutes to the current time in UTC."""
    now = datetime.now(timezone.utc)  # Ensure UTC timezone
    future_time = now + timedelta(minutes=32)
    return future_time.isoformat()  # This will return in the format "2025-03-26T18:10:46+00:00"

# Example output: "2025-03-26T19:00:00+00:00"


def create_auction():
    """Creates an auction with the given document ID."""
    # Step 1: Get the token by logging in
    token = api_login_organiser()  # Use the api_login function to get the token
    document_id = upload_document()

    # Step 2: Prepare auction data
    fast_time = generate_fast_manual_time()  # Generate fast manual time
    url = f"{ConfigParser.base_url}/api/v1.0/auctions"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    auction_data = {
        "bankAccounts": [
            {
                "type": "GUARANTEE",
                "bankAccounts": [
                    {
                        "bankName": "mono",
                        "currency": "UAH",
                        "holderLegalName": "Brandon",
                        "holderIdentifierScheme": "UA-EDR",
                        "holderIdentifier": "00120145",
                        "identifiers": [
                            {
                                "scheme": "UA-IBAN",
                                "id": "UA121111110000012001234567896"
                            }
                        ]
                    }
                ]
            }
        ],
        "attempts": 1,
        "description": "sadfas dasd fasdfs",
        "name": "Automation",
        "subtype": "FAST_MANUAL",
        "type": "BASIC_SELL_ENGLISH",
        "userProfileId": 73,
        "startedAt": fast_time,  # Use the generated fast time
        "lotNumber": "1",
        "accessDetails": None,
        "currency": "UAH",
        "initialAmount": 1200,
        "includePdv": True,
        "specificData": {
            "documentRequirements": None,
            "additionalInformation": None,
            "valueAddedTaxCharged": False,
            "guaranteeAmount": 360,
            "registrationAmount": 17,
            "lots": [
                {
                    "address": {
                        "city": "Красностав",
                        "country": "Україна",
                        "region": "Хмельницька область",
                        "addressID": "0500000000",
                        "zipCode": "30085",
                        "street": None
                    },
                    "additionalClassifications": [],
                    "cav": "19000000-6",
                    "description": "asd asd fsdfs",
                    "measureUnit": "IE",
                    "quantity": 43,
                    "location": {
                        "latitude": 50.40118706890082,
                        "longitude": 27.180175781250004
                    },
                    "props": None
                }
            ],
            "isPerishable": False,
            "stepAmount": 14.4,
            "minNumberOfQualifiedBids": 2
        },
        "documents": [
            {
                "id": document_id  # Attach the document ID
            }
        ]
    }

    # Step 3: Send the POST request to create the auction
    response = requests.post(url, json=auction_data, headers=headers)

    # Step 4: Handle response and extract auction ID
    if response.status_code == 200:
        json_data = response.json()
        auction_id = json_data.get("id")
        print(f"Auction created successfully. Auction ID: {auction_id}")
        return auction_id
    else:
        raise Exception(f"Failed to create auction: {response.status_code}, {response.text}")


def publish_auction():
    """Publishes the auction with the given draft ID."""
    # Step 1: Get the token by logging in
    token = api_login_organiser()  # Use the api_login function to get the token
    draft_id = create_auction()

    # Step 2: Prepare the URL and headers
    url = f"{ConfigParser.base_url}/api/v1.0/auctions/{draft_id}/publish"
    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Step 3: Send the POST request to publish the auction
    response = requests.post(url, headers=headers)

    # Step 4: Handle response
    if response.status_code == 200:
        print(f"Auction {draft_id} published successfully.")
        return response.json()  # You can return the response if needed
    else:
        raise Exception(f"Failed to publish auction {draft_id}: {response.status_code}, {response.text}")

def create_bid(auction_id, user_profile_id=62, initial_amount=1500):
    """
    Creates a bid (draft application) for a given auction via API.

    Args:
        auction_id (str): ID of the auction for which the bid is being created.
        user_profile_id (int): User profile ID of the bidder.
        initial_amount (float): Initial amount offered in the bid.

    Returns:
        str: ID of the created bid.
    """
    token = api_login_participant()  # Make sure this logs in a bidder

    url = f"{ConfigParser.base_url}/api/v1.0/bids"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "auctionId": auction_id,
        "userProfileId": user_profile_id,
        "initialAmount": initial_amount
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        bid_id = response.json().get("id")
        print(f"Bid created successfully. Bid ID: {bid_id}")
        return bid_id
    else:
        raise Exception(f"Failed to create bid: {response.status_code}, {response.text}")

def publish_bid(bid_id):
    """
    Publishes a bid (application) using the PATCH method.

    Args:
        bid_id (str): ID of the bid to be published.

    Returns:
        dict: JSON response from the server.
    """
    token = api_login_participant()  # Same as for create_bid

    url = f"{ConfigParser.base_url}/api/v1.0/bids/{bid_id}/publish"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.patch(url, headers=headers)

    if response.status_code == 200:
        print(f"Bid published successfully. Bid ID: {bid_id}")
        return response.json()
    else:
        raise Exception(f"Failed to publish bid: {response.status_code}, {response.text}")

