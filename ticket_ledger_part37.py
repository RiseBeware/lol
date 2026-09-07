# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: TicketLedger
import unittest
from ticketledger import TicketLedger

class TicketLedgerTests(unittest.TestCase):
    def setUp(self):
        self.ledger = TicketLedger()

    def test_create_ticket(self):
        t = self.ledger.create_ticket("Test", "Bug", "P1", "dev1", "2025-04-01", "Fixed")
        self.assertEqual(t.id, 1)
        self.assertEqual(t.title, "Test")
        self.assertEqual(t.status, "Solved")

    def test_ticket_ids_increment(self):
        self.ledger.create_ticket("A", "Bug", "P1", "dev1", "2025-04-01", "Fixed")
        self.ledger.create_ticket("B", "Request", "P2", "dev2", "2025-04-02", "In Progress")
        self.assertEqual(self.ledger.get_ticket(1).id, 1)
        self.assertEqual(self.ledger.get_ticket(2).id, 2)

    def test_status_transitions(self):
        t = self.ledger.create_ticket("T", "Bug", "P1", "dev1", "2025-04-01", "Open")
        self.assertEqual(t.status, "Open")
        t.status = "In Progress"
        self.assertEqual(t.status, "In Progress")
        t.status = "Solved"
        self.assertEqual(t.status, "Solved")

    def test_get_ticket_by_id_not_found(self):
        self.assertIsNone(self.ledger.get_ticket(999))

    def test_list_tickets_empty(self):
        self.assertEqual(self.ledger.list_tickets(), [])

    def test_list_tickets_after_add(self):
        self.ledger.create_ticket("T1", "Bug", "P1", "dev1", "2025-04-01", "Open")
        self.assertEqual(len(self.ledger.list_tickets()), 1)

if __name__ == "__main__":
    unittest.main()
