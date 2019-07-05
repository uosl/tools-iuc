from __future__ import print_function
import sys
import intermine
from intermine.webservice import Service

service = Service("http://www.humanmine.org/humanmine/service")
query = service.new_query("Gene")
query.add_view("symbol")
query.add_constraint("symbol", "=", sys.argv[1], code = "A")

print("symbol")
for row in query.rows():
    print(row["symbol"])

