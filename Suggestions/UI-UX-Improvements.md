# Suggestions & UI/UX Improvements — Demo Web Shop

This document captures usability observations and improvement recommendations that are **not functional bugs**, but affect user experience and clarity.

---

## SUGG-001

| Field | Details |
|---|---|
| **Suggestion ID** | SUGG-001 |
| **Related Bug** | [BUG-001](../Bug-Reports/Bug-Reports.md#bug-001) |
| **Module** | Books |
| **Observation** | Some products on the Books listing page do not show an "Add to Cart" button, and there is no message indicating stock status (e.g., "Out of Stock," "Currently Unavailable," "Coming Soon"). |
| **Impact on User** | Users may assume the product is broken, the page failed to load correctly, or simply feel confused about why they cannot purchase the item — leading to a poor browsing experience and potential loss of trust in the platform. |
| **Recommendation** | Display a clear status label (e.g., a greyed-out "Out of Stock" button or a small badge like "Unavailable") in place of the missing "Add to Cart" button, so users always understand product availability at a glance. |
| **Suggested Priority** | Medium — improves clarity and overall UX without requiring core functional changes |
| **Category** | Usability / Communication Gap |

---

## SUGG-002

| Field | Details |
|---|---|
| **Suggestion ID** | SUGG-002 |
| **Related Bug** | N/A |
| **Module** | Shopping Cart |
| **Observation** | The cart page does not have a dedicated "Remove" button per item. To remove a product, the user must check a small checkbox in the "Remove" column, then click the separate "Update shopping cart" button — a 2-step process. |
| **Impact on User** | Users familiar with a single-click "Remove" (common on most e-commerce sites) may not realize they need to check the box AND click Update — leading to confusion or accidental cart changes. |
| **Recommendation** | Add a direct "Remove" icon/button next to each cart item that removes it immediately on click, without needing a separate checkbox + update step. |
| **Suggested Priority** | Low — usability improvement, not a functional issue |
| **Category** | Usability |

---

*Additional suggestions will be logged here as more areas of the application are explored.*
