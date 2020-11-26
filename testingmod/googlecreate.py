from gcsa.event import Event

event = Event(
    'The Glass Menagerie',
    start=datetime(2020, 7, 10, 19, 0),
    location='Záhřebská 468/21'
    minutes_before_popup_reminder=15
)
calendar.add_event(event)
