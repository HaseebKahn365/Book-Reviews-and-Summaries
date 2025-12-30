from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:15000')

print(s.add(22,2))
# print(s.div(32,3)) //force divs by 0 in server