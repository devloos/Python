
from typing import Self


class Task:
    def __init__(self, desc: str, date: str, time: str):
        self.description = desc
        self.date = date
        self.time = time

    def get_description(self):
        return self.description

    def __str__(self):
        return f"{self.description} - Due: {self.date} at {self.time}"

    def __repr__(self):
        return f"{self.description},{self.date},{self.time}"

    def __lt__(self, other: Self):
        self_month, self_day, self_year = map(int, self.date.split('/'))
        self_hour, self_minute = map(int, self.time.split(':'))

        other_month, other_day, other_year = map(int, other.date.split('/'))
        other_hour, other_minute = map(int, other.time.split(':'))

        if self_year != other_year:
            return self_year < other_year

        if self_month != other_month:
            return self_month < other_month

        if self_day != other_day:
            return self_day < other_day

        if self_hour != other_hour:
            return self_hour < other_hour

        if self_minute != other_minute:
            return self_minute < other_minute

        return self.description < other.description
