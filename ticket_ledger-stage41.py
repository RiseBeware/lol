# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: TicketLedger
def _dry_run_mode():
    """Toggle dry-run mode. When active, mutating operations are logged and skipped."""
    global _dry_run
    _dry_run = not _dry_run
    if _dry_run:
        print("[DRY-RUN MODE] Mutations are simulated. No changes will be persisted.")
    return _dry_run
