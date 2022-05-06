from datetime import datetime


class Meeting:
    def __init__(self, date: datetime, title: str):
        self.date = date
        self.title = title


class Calendar:
    def __init__(self):
        self.meetings = {}

    def add_meeting(self, meeting: Meeting):
        if meeting.date not in self.meetings:
            self.meetings[meeting.date] = meeting


def test_add_meeting():
    # given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), 'My birthday!')
    birthday2 = Meeting(datetime(2020, 11, 9, 12, 0), 'My birthday!')
    calendar = Calendar()
    # when
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)
    # then
    assert len(calendar.meetings) == 1


