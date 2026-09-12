# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: TicketLedger
def main():
    import argparse
    parser = argparse.ArgumentParser(description="TicketLedger CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_create = sub.add_parser("create")
    p_create.add_argument("--ticket", "-t", required=True)
    p_create.add_argument("--category", "-c", default="general")
    p_create.add_argument("--priority", "-p", default="medium")
    p_create.add_argument("--assignee", "-a", default=None)
    p_create.add_argument("--deadline", "-d", default=None)

    p_show = sub.add_parser("show")
    p_show.add_argument("--ticket", "-t", default=None)

    p_list = sub.add_parser("list")
    p_list.add_argument("--category", "-c", default=None)
    p_list.add_argument("--priority", "-p", default=None)

    p_update = sub.add_parser("update")
    p_update.add_argument("--ticket", "-t", required=True)
    p_update.add_argument("--status", "-s", default=None)
    p_update.add_argument("--resolution", "-r", default=None)

    p_delete = sub.add_parser("delete")
    p_delete.add_argument("--ticket", "-t", required=True)

    args = parser.parse_args()

    tickets = load_tickets()
    if args.cmd == "create":
        t = {
            "ticket": args.ticket,
            "category": args.category,
            "priority": args.priority,
            "assignee": args.assignee,
            "deadline": args.deadline,
            "status": "open",
            "resolution": None,
        }
        tickets[t["ticket"]] = t
        save_tickets(tickets)
        print(f"Created ticket {args.ticket}")
    elif args.cmd == "show":
        if args.ticket:
            t = tickets.get(args.ticket)
            if t:
                print(f"Ticket: {t}")
            else:
                print(f"Ticket {args.ticket} not found")
        else:
            print(tickets)
    elif args.cmd == "list":
        filtered = tickets
        if args.category:
            filtered = {k: v for k, v in filtered.items() if v["category"] == args.category}
        if args.priority:
            filtered = {k: v for k, v in filtered.items() if v["priority"] == args.priority}
        print(filtered)
    elif args.cmd == "update":
        t = tickets.get(args.ticket)
        if not t:
            print(f"Ticket {args.ticket} not found")
            return
        if args.status:
            t["status"] = args.status
        if args.resolution:
            t["resolution"] = args.resolution
        save_tickets(tickets)
        print(f"Updated ticket {args.ticket}")
    elif args.cmd == "delete":
        if args.ticket in tickets:
            del tickets[args.ticket]
            save_tickets(tickets)
            print(f"Deleted ticket {args.ticket}")
        else:
            print(f"Ticket {args.ticket} not found")
