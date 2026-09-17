# === Stage 43: Добавь пагинацию длинных списков ===
# Project: TicketLedger
def paginate(items, page=1, per_page=10):
    total = len(items)
    start = (page - 1) * per_page
    end = start + per_page
    page_items = items[start:end]
    return {
        "items": page_items,
        "total": total,
        "page": page,
        "per_page": per_page,
        "pages": (total + per_page - 1) // per_page if total else 0,
        "has_next": page < (total + per_page - 1) // per_page if total else False,
        "has_prev": page > 1,
    }
