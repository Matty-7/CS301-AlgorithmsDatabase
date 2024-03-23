#!/opt/homebrew/bin/python3.11

import sys, os
cwd = os.path.dirname(__file__)

jarfile = cwd + '/'+ 'repolab_sag_client.jar'

cmd = 'java --enable-preview -jar %s ' % jarfile
#cmd = 'java  -jar %s ' % jarfile
print(cmd)
print("Run SAG client: %s" % os.path.abspath(__file__))
cmd = cmd+  ' '.join(sys.argv[1:])
print(cmd)
os.system(cmd)
