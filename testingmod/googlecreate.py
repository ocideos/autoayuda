from gcsa.event import Event

event = Event(
    'Grupo Autoayuda 1',
    start=datetime(2020, 12, 12, 9, 0),
    location='Ciudad Mujer tegucigalpa-Google meets'
    minutes_before_popup_reminder=15
)
calendar.add_event(event)
