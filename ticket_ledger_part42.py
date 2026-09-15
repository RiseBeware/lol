# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: TicketLedger
# ANSI colour support – toggleable via environment variable or CLI flag
try:
    import colorama
    colorama.init(autoreset=True)
except ImportError:
    colorama = None

def _colour_enabled():
    return (
        colorama is not None
        and os.environ.get("TICKETLEDGER_NO_ANSI", "").lower() not in ("1", "true")
        and os.environ.get("TERM", "").lower() not in ("dumb", "")
    )

class _Col:
    _reset = "\033[0m"
    _red = "\033[31m"
    _green = "\033[32m"
    _yellow = "\033[33m"
    _blue = "\033[34m"
    _magenta = "\033[35m"
    _cyan = "\033[36m"
    _white = "\033[37m"
    _bold = "\033[1m"

    def __init__(self, on):
        self.on = on

    def r(self, text):    return self.on + self._red + text + self._reset
    def g(self, text):    return self.on + self._green + text + self._reset
    def y(self, text):    return self.on + self._yellow + text + self._reset
    def b(self, text):    return self.on + self._blue + text + self._reset
    def m(self, text):    return self.on + self._magenta + text + self._reset
    def c(self, text):    return self.on + self._cyan + text + self._reset
    def w(self, text):    return self.on + self._white + text + self._reset
    def bold(self, text): return self.on + self._bold + text + self._reset

def colour(text, kind):
    """Return coloured text for a ticket kind or plain text if disabled."""
    if not _colour_enabled():
        return text
    return {
        "info":    _Col(True).c(text),
        "warning": _Col(True).y(text),
        "error":   _Col(True).r(text),
        "success": _Col(True).g(text),
    }.get(kind, text)
