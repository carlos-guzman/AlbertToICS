from datetime import datetime
from event import Event
import StringIO

def decode_time(raw):
    times = raw.split(":")
    if times[1][-2:] == "PM" and times[0] != "12":
        hour = str(int(times[0])+12)
    else:
        hour = times[0]

    if len(hour)<2:
        hour = "0"+hour

    return hour+times[1][:2]+"00"


def parse(text):
    # input = StringIO.StringIO()
    # if input.readline()[:4].lower() == "this":
    #     input.readline()
    # next = input.readline()
    
    events = []
    
    events_str = text.split("Academic Calendar Deadlines\n")
    events_str.pop(0)
    for e in events_str:
        event = e.split("\n")

        times = event[2].upper().split(" ", 1)

        start = decode_time(times[1].split(" - ")[0])
        end = decode_time(times[1].split(" - ")[1])

        events.append(Event(event[0], 
            event[3].replace(" Room:", "- ").lstrip("Bldg:"),
             start, end, [times[0][i:i+2] for i in range(0, len(times[0]), 2)], event[1]))

    print len(events), " events have been parsed\n"

    return events


def write_calendar(
        events, file=open("schedule.ics", "w"), cal_name="My Schedule"):
    file.write("BEGIN:VCALENDAR\r\n"+
        "VERSION:2.0\r\n"+
        "PRODID:-//Carlos Guzman//Guzman Calendar v1.0//EN\r\n"+
        "CALSCALE:GREGORIAN\r\n"+
        "METHOD:PUBLISH\r\n"+
        "X-WR-CALNAME:"+cal_name+"\r\n"+
        "X-WR-TIMEZONE:America/New_York\r\n"+
        "BEGIN:VTIMEZONE\r\n"+
        "TZID:America/New_York\r\n"+
        "X-LIC-LOCATION:America/New_York\r\n"+
        "BEGIN:DAYLIGHT\r\n"+
        "TZOFFSETFROM:-0500\r\n"+
        "TZOFFSETTO:-0400\r\n"+
        "TZNAME:EDT\r\n"+
        "DTSTART:19700308T020000\r\n"+
        "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU\r\n"+
        "END:DAYLIGHT\r\n"+
        "BEGIN:STANDARD\r\n"+
        "TZOFFSETFROM:-0400\r\n"+
        "TZOFFSETTO:-0500\r\n"+
        "TZNAME:EST\r\n"+
        "DTSTART:19951215T191200\r\n"+
        "RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU\r\n"+
        "END:STANDARD\r\n"+
        "END:VTIMEZONE\r\n");

    current_date = datetime.now().strftime("%Y%m%dT%H%M%SZ")


    for event in events:
        weekdays = ""
        for day in event.weekdays:
            weekdays += day+","
        weekdays = weekdays[:-1]


        w.write("BEGIN:VEVENT\r\n"+
            "DTSTART;TZID=America/New_York:20140901T"+event.start+"\r\n"+
            "EXDATE;TZID=America/New_York:20140901T"+event.start+"\r\n"+
            "DTEND;TZID=America/New_York:20140901T"+event.end+"\r\n"+
            "RRULE:FREQ=WEEKLY;UNTIL=20141218T170000Z;BYDAY="+weekdays+"\r\n"+
            "CREATED:"+current_date+"\r\n"+
            "DESCRIPTION:"+event.description+"\r\n"+
            "LAST-MODIFIED:"+current_date+"\r\n"+
            "LOCATION:"+event.place+"\r\n"+
            "SEQUENCE:0\r\n"+
            "STATUS:CONFIRMED\r\n"+
            "SUMMARY:"+event.name+"\r\n"+
            "TRANSP:OPAQUE\r\n"+
            "END:VEVENT\r\n")

    w.write("END:VCALENDAR")
    w.close()

    print len(events), " events have been successfully added to the calendar\n"

    return


r = open("schedule", "r")
events = parse(r.read())

    # "This Week's Schedule\n"+
    # "Class   Schedule\n"+
    # "Academic Calendar Deadlines\n"+
    # "CORE-UA 536-001\n"+
    # "LEC (18164)\n"+
    # "TuTh 9:30AM - 10:45AM\n"+
    # "Bldg:SILV  Room:207")


#events = [Event("Name", "Somewhere", "012345", "123456", ["MO", "WE"])]


w = open("test.ics", "w")
write_calendar(events, w)





#r.close()

