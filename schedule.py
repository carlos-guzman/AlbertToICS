from datetime import datetime
from event import Event

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

    d = datetime.now().strftime("%Y%m%dT%H%M%SZ")

    for event in events:
        w.write("BEGIN:VEVENT\r\n"+
            "DTSTART;TZID=America/New_York:20140910T"+event.start+"\r\n"+
            "DTEND;TZID=America/New_York:20140910T"+event.end+"\r\n"+
            "RRULE:FREQ=WEEKLY;UNTIL=20141218T170000Z;BYDAY=MO,TU,WE,TH\r\n"+
            "CREATED:"+d+"\r\n"+
            "DESCRIPTION:\r\n"+
            "LAST-MODIFIED:"+d+"\r\n"+
            "LOCATION:\r\n"+
            "SEQUENCE:0\r\n"+
            "STATUS:CONFIRMED\r\n"+
            "SUMMARY:Bus\r\n"+
            "TRANSP:OPAQUE\r\n"+
            "END:VEVENT\r\n")

    w.write("END:VCALENDAR")
    w.close()

    return


#r = open("nyubuse", "r")

events = [Event("Name", "Somewhere", "012345", "123456", ["MO", "WE"])]


w = open("test.ics", "w")
write_calendar(events, w)





#r.close()

