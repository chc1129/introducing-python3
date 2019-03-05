import os

os.chmod('oops.txt', 0o400)

import stat
os.chmod('oops.txt', stat.S_IRUSR)

uid = 5
gid = 22
os.chown('oops.txt', uid, gid)
