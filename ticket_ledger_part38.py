# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: TicketLedger
import unittest

class TestTicketEdgeCases(unittest.TestCase):
    def test_ticket_with_no_fields(self):
        ticket = Ticket()
        self.assertEqual(ticket.id, 0)
        self.assertEqual(ticket.title, "")
        self.assertEqual(ticket.description, "")
        self.assertEqual(ticket.priority, "low")
        self.assertEqual(ticket.status, "open")
        self.assertEqual(ticket.assigned_to, None)
        self.assertEqual(ticket.category, None)
        self.assertEqual(ticket.due_date, None)
        self.assertEqual(ticket.resolution, None)
        self.assertEqual(ticket.created_at, None)
        self.assertEqual(ticket.updated_at, None)

    def test_ticket_with_all_fields(self):
        ticket = Ticket(
            id=1,
            title="Test Ticket",
            description="Test Description",
            priority="high",
            status="open",
            assigned_to="John",
            category="bug",
            due_date="2024-12-31",
            resolution="fixed",
            created_at="2024-01-01",
            updated_at="2024-06-30"
        )
        self.assertEqual(ticket.id, 1)
        self.assertEqual(ticket.title, "Test Ticket")
        self.assertEqual(ticket.description, "Test Description")
        self.assertEqual(ticket.priority, "high")
        self.assertEqual(ticket.status, "open")
        self.assertEqual(ticket.assigned_to, "John")
        self.assertEqual(ticket.category, "bug")
        self.assertEqual(ticket.due_date, "2024-12-31")
        self.assertEqual(ticket.resolution, "fixed")
        self.assertEqual(ticket.created_at, "2024-01-01")
        self.assertEqual(ticket.updated_at, "2024-06-30")

    def test_ticket_with_none_fields(self):
        ticket = Ticket(
            id=1,
            title=None,
            description=None,
            priority=None,
            status=None,
            assigned_to=None,
            category=None,
            due_date=None,
            resolution=None,
            created_at=None,
            updated_at=None
        )
        self.assertEqual(ticket.id, 1)
        self.assertIsNone(ticket.title)
        self.assertIsNone(ticket.description)
        self.assertIsNone(ticket.priority)
        self.assertIsNone(ticket.status)
        self.assertIsNone(ticket.assigned_to)
        self.assertIsNone(ticket.category)
        self.assertIsNone(ticket.due_date)
        self.assertIsNone(ticket.resolution)
        self.assertIsNone(ticket.created_at)
        self.assertIsNone(ticket.updated_at)

if __name__ == '__main__':
    unittest.main()
