attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]


def generate_invitations(template, attendees):
    if not isinstance(template, str) or isinstance(attendees, list):
        raise TypeError("Be sure the templates is a string or attendees is a list.")
    if len(template) == 0:
        raise ValueError("Template is empty")
    if len(attendees) == 0:
        raise ValueError("Attendees is empty")



generate_invitations(template, attendees)
