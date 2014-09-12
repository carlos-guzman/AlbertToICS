from datetime import datetime

r = open("nyubuse", "r")
w = open("buses.ics", "w")

w.write("BEGIN:VCALENDAR\n"+
"CALSCALE:GREGORIAN\n"+
"METHOD:PUBLISH\n"+
"X-WR-CALNAME:My Schedule"+"\n"+
"X-WR-TIMEZONE:America/New_York\n"+
"BEGIN:VTIMEZONE\n"+
"TZID:America/New_York\n"+
"X-LIC-LOCATION:America/New_York\n"+
"BEGIN:DAYLIGHT\n"+
"TZOFFSETFROM:-0500\n"+
"TZOFFSETTO:-0400\n"+
"TZNAME:EDT\n"+
"DTSTART:19700308T020000\n"+
"RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU\n"+
"END:DAYLIGHT\n"+
"BEGIN:STANDARD\n"+
"TZOFFSETFROM:-0400\n"+
"TZOFFSETTO:-0500\n"+
"TZNAME:EST\n"+
"DTSTART:19701101T020000\n"+
"RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU\n"+
"END:STANDARD\n"+
"END:VTIMEZONE\n");

d = datetime.now().strftime("%Y%m%dT%H%M%SZ")

for time in r:
    w.write("BEGIN:VEVENT\n"+
"DTSTART;TZID=America/New_York:20140910T"+time+
"DTEND;TZID=America/New_York:20140910T"+time+
"RRULE:FREQ=WEEKLY;UNTIL=20141218T170000Z;BYDAY=MO,TU,WE,TH\n"+
"CREATED:"+d+"\n"+
"DESCRIPTION:\n"+
"LAST-MODIFIED:"+d+"\n"+
"LOCATION:\n"+
"SEQUENCE:0\n"+
"STATUS:CONFIRMED\n"+
"SUMMARY:Bus\n"+
"TRANSP:OPAQUE\n"+
"END:VEVENT\n")

w.write("END:VCALENDAR")

r.close()
w.close()