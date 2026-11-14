# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: TicketLedger
def export_report(records, categories, priorities, assignees, due_dates, resolutions):
    lines = []
    lines.append("TICKET LEDGER - КРАТКИЙ ОТЧЁТ")
    lines.append("=" * 40)
    lines.append(f"Всего заявок: {len(records)}")
    lines.append("")
    lines.append("Категории:")
    for cat in categories:
        lines.append(f"  - {cat}")
    lines.append("")
    lines.append("Приоритеты:")
    for pr in priorities:
        lines.append(f"  - {pr}")
    lines.append("")
    lines.append("Исполнители:")
    for asg in assignees:
        lines.append(f"  - {asg}")
    lines.append("")
    lines.append("Сроки:")
    for due in due_dates:
        lines.append(f"  - {due}")
    lines.append("")
    lines.append("Решения:")
    for res in resolutions:
        lines.append(f"  - {res}")
    lines.append("")
    lines.append("Детализация:")
    for i, rec in enumerate(records, 1):
        lines.append(f"  {i}. {rec}")
    report = "\n".join(lines)
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    return report
