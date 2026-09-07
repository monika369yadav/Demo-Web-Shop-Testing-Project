# Bug Reports — Demo Web Shop

This document lists confirmed functional/UI bugs found during manual testing. Each entry follows a standard professional bug-reporting format.

> **Note:** Not every observation is a "bug." Issues are classified as a **Bug** only when they break expected functionality. Cosmetic, usability, or communication gaps that don't break functionality are logged separately under [UI/UX Improvements](../Suggestions/UI-UX-Improvements.md).

---

## BUG-001

| Field | Details |
|---|---|
| **Bug ID** | BUG-001 |
| **Title** | Missing "Add to Cart" button and no stock-status message across multiple product categories |
| **Module** | Books, Computers (Desktops), Electronics (Camera/Photo, Cell Phones) |
| **Description** | Several products across multiple categories do not display an "Add to Cart" button. There is also no alternative message such as "Out of Stock" or "Currently Unavailable" to inform the user why the option is missing. This was initially found in the Books category, but further testing confirmed the same issue occurs in Computers and Electronics categories as well — indicating this is a site-wide pattern, not limited to one category. |
| **Steps to Reproduce** | 1. Navigate to any of the affected categories (Books, Computers → Desktops, Electronics → Camera/Photo, Electronics → Cell phones) 2. Observe the product grid 3. Note that some products show a price and rating but no "Add to Cart" button |
| **Test Data** | Affected products: Fiction, Fiction EX (Books); Desktop PC with CDRW, Elite Desktop PC, Simple Computer (Desktops); 1MP 60GB Hard Drive Handycam Camcorder, Camcorder, Digital SLR Camera 12.2 Mpixel, High Definition 3D Camcorder (Camera/Photo — all 4 products in this category are affected); Used phone (Cell phones) |
| **Expected Result** | Every product should either show an "Add to Cart" button (if purchasable) or a clear status message explaining why it cannot be purchased |
| **Actual Result** | Affected products display price and rating, but no purchase option and no explanation is shown, across multiple categories |
| **Severity** | High *(escalated from Medium — this is not a one-off issue, it repeats across at least 3 separate categories, impacting the core purchase flow site-wide)* |
| **Priority** | High |
| **Environment** | Chrome, Desktop, Demo Web Shop (demowebshop.tricentis.com) |
| **Screenshots** | See `/Screenshots/Defects/BUG-001.png` (Books), `/Screenshots/Defects/BUG-001-2.png` (Desktops), `/Screenshots/Defects/BUG-001-3.png` (Camera/Photo) |
| **Status** | Open |

**QA Note:** This was evaluated for classification — since it does not break any functionality (the page loads fine, no error occurs) but creates user confusion about product availability, it has also been cross-logged as a UI/UX improvement recommendation. See [SUGG-001](../Suggestions/UI-UX-Improvements.md#sugg-001).

---

## BUG-002

| Field | Details |
|---|---|
| **Bug ID** | BUG-002 |
| **Title** | Manufacturer page ("Tricentis") displays empty content with no products or message |
| **Module** | Manufacturer / Navigation |
| **Description** | Clicking on the "Tricentis" manufacturer link (left sidebar, under Manufacturers) loads a page showing only the heading "Tricentis" with no products listed and no message such as "No products found" to explain the empty state. |
| **Steps to Reproduce** | 1. Log in / browse as any user 2. In the left sidebar, click "Tricentis" under Manufacturers 3. Observe the page content |
| **Test Data** | Manufacturer: Tricentis |
| **Expected Result** | Page should either show all products from this manufacturer, or a clear message like "No products found for this manufacturer" |
| **Actual Result** | Page loads with only the "Tricentis" heading; no products and no explanatory message shown |
| **Severity** | Low *(page doesn't crash, but creates confusion for the user)* |
| **Priority** | Low |
| **Environment** | Chrome, Desktop, Demo Web Shop (demowebshop.tricentis.com) |
| **Screenshots** | See `/Screenshots/Defects/BUG-002.png` |
| **Status** | Open |

---

## BUG-003

| Field | Details |
|---|---|
| **Bug ID** | BUG-003 |
| **Title** | Search functionality returns "No products found" for all keywords, including valid category names |
| **Module** | Search |
| **Description** | The site search does not return any results, even when searching for exact, existing category names such as "Books", "Computers", "Electronics", and "Gift cards" — all of which are visible in the site's own navigation menu. This indicates the search functionality is not indexing or matching products/categories correctly, making it effectively unusable. |
| **Steps to Reproduce** | 1. Log in / browse the site 2. Use the "Search store" box (or Search page) 3. Enter a known valid keyword such as "Books" 4. Click Search |
| **Test Data** | Keywords tested: Books, Computers, Electronics, Gift cards |
| **Expected Result** | Search should return relevant products or categories matching the keyword |
| **Actual Result** | "No products were found that matched your criteria" is shown for every keyword tested, even valid category names |
| **Severity** | Critical *(a completely non-functional search breaks a core feature used by nearly every shopper)* |
| **Priority** | High |
| **Environment** | Chrome, Desktop, Demo Web Shop (demowebshop.tricentis.com) |
| **Screenshots** | See `/Screenshots/Defects/BUG-003.png` (Electronics), `/Screenshots/Defects/BUG-003-2.png` (Gift cards), `/Screenshots/Defects/BUG-003-3.png` (Books), `/Screenshots/Defects/BUG-003-4.png` (Computers) |
| **Status** | Open |

---

## BUG-004

| Field | Details |
|---|---|
| **Bug ID** | BUG-004 |
| **Title** | State/Province field does not show actual states when Country = India |
| **Module** | Checkout / Billing Address |
| **Description** | On the Billing Address step of checkout, selecting "India" as the Country does not populate the State/province dropdown with actual Indian states (e.g., Delhi, Maharashtra, Haryana). Instead, it only shows a generic option "Other (Non US)". |
| **Steps to Reproduce** | 1. Go to Checkout → Billing Address 2. Select Country = India 3. Check the State/province dropdown |
| **Test Data** | Country: India |
| **Expected Result** | State/province dropdown should list actual Indian states to choose from |
| **Actual Result** | Only "Other (Non US)" is available; no real state list is shown |
| **Severity** | Low *(does not block checkout, but affects address accuracy)* |
| **Priority** | Low |
| **Environment** | Chrome, Desktop, Demo Web Shop (demowebshop.tricentis.com) |
| **Screenshots** | See `/Screenshots/Defects/BUG-004.png` |
| **Status** | Open |

---

*New bugs will be added here as testing progresses, following the same format.*
