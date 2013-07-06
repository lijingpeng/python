#!/usr/bin/env python
import cgi

print "Content-Type:text/html\r\n\r\n"
print("<html>")  
print("<head><title>Hello,python</title></head>")
print("<body><h1>hello, i am " )

form = cgi.FieldStorage()
who = form[ 'person' ].value
howmany = form[ 'howmany' ].value
print "<INPUT type=text value=" + who + "size=15>"
print("</h1></body>")  
print("</html>")  
