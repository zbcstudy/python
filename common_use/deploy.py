#!/usr/bin/env python

import sys
import os
import signal
import time


def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


args = sys.argv
args = args[args.index(__file__)+1:]
name = args[0]
jar = args[1]
if not name:
    print('No name arg')
if not jar:
    print('No jar arg')
if os.path.exists(name):
    if not os.path.isdir(name):
        sys.exit("[%s] is exists and not dir" % name)
else:
    os.mkdir(name)
if os.path.isfile("%s/%s" % (name, jar)):
    os.rename("%s/%s" % (name, jar), "%s/%s.latest" % (name, jar))
os.rename(jar, "%s/%s" % (name, jar))
pid_filename = "%s/pid" % name
latest_pid_filename = pid_filename+".latest"
if os.path.exists(pid_filename):
    pid_file = open(pid_filename, 'r')
    pid = pid_file.read()
    os.rename(pid_filename, latest_pid_filename)
    os.kill(pid, signal.SIGSTOP)
    msg = 'waiting process down'
    while check_pid(pid):
        msg = msg+"."
        print(msg+"\r")
        time.sleep(1)
output_filename = "%s/output" % name
latest_output_filename = output_filename+".latest"
if os.path.exists(output_filename):
    os.rename(output_filename, latest_output_filename)

# nohup java -jar "$name/$jar" > "$name/output" 2>&1 &
# echo $! > "$name/pid"
# echo "running $jar in [$(cat $name/pid)]"
