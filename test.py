from modules.logger import Logger
from time import sleep

log = Logger()
log.start()
log.info('This is a INFO text')
if log.checklog('criticals'):
    print('No criticals')
else:
    print('Criticals in logfile')
if log.checklog('warnings'):
    print('No warnings')
else:
    print('Warnings in logfile')
if log.checklog('both'):
    print('No warnings or criticals')
else:
    print('Warnings or Criticals in logfile')
sleep(1)
log.warning('This is a WARNING text')
sleep(1)
log.critical('This is a CRITICAL text')

if log.checklog('criticals'):
    print('No criticals')
else:
    print('Criticals in logfile')
if log.checklog('warnings'):
    print('No warnings')
else:
    print('Warnings in logfile')
if log.checklog('both'):
    print('No warnings or criticals')
else:
    print('Warnings or Criticals in logfile')

log.end()

print(log.__doc__)