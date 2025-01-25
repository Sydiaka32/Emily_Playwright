import pytest
from playwright.async_api import Playwright, APIRequestContext, async_playwright
import asyncio

# Fixture for initializing Playwright (Async API)
@pytest.fixture(scope="session")
async def playwright() -> Playwright:
    async with async_playwright() as p:
        yield p

# Fixture for APIRequestContext using Async API
@pytest.fixture(scope="session")
async def api_request_context(playwright: Playwright) -> APIRequestContext:
    request_context = await playwright.request.new_context(
        base_url="https://qa.ualand.utest.pro/api/v1.0/auctions/search/created/short"
    )
    yield request_context
    await request_context.dispose()
