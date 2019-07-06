from __future__ import print_function
import sys
from intermine.webservice import Service

service = Service(sys.argv[1]+"/service")
query = service.new_query("Gene")
query.add_view("symbol")
query.add_constraint("symbol", "=", sys.argv[2], code = "A")

print("symbol")
for row in query.rows():
    print(row["symbol"])

