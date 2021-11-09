from datetime import datetime

class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d").date()

    def to_url(self, value):
        return str(value)
