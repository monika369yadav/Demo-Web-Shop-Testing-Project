"""
Test Suite: Search
Covers manual Test Case: TC-015 (search should return relevant results)

This test asserts the CORRECT expected behavior. It is marked as an expected
failure (xfail) because BUG-003 is a known, currently-open defect: search
returns "No products found" even for valid, existing category names.
Once BUG-003 is fixed, this test should be updated by removing the xfail
marker, at which point it will start passing and confirm the fix.
"""

import pytest
from pages.search_page import SearchPage


@pytest.mark.xfail(reason="BUG-003: Search returns no results even for valid keywords")
@pytest.mark.parametrize("keyword", ["Books", "Computers", "Electronics", "Gift cards"])
def test_search_returns_results_for_valid_keyword(driver, keyword):
    """TC-015: Verify search returns relevant results for a valid, existing keyword."""
    search_page = SearchPage(driver)
    search_page.open()
    search_page.search_for(keyword)

    assert not search_page.has_no_results_message(), (
        f"Expected results for '{keyword}', but 'No products found' was shown"
    )
    assert search_page.get_result_count() > 0
