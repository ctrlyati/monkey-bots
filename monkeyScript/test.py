from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time

STATE_IDLE = 0
STATE_START_CLICK = 1
STATE_RUN_CLICK = 2
STATE_EXIT = 3

state = STATE_IDLE

def run_click(threadName, delay):
	state = STATE_RUN_CLICK
	while state==STATE_RUN_CLICK:
		device.touch(000, 800, 'DOWN_AND_UP');
		time.sleep(delay)

def help():
	print 'This is help...'
	print '\tCOMMAND\tDESCRIPTION'
	print '\tstart\tgoing to start clicking loop'
	print '\texit\texit the program'
	print ''

print "____________________________________"

print "waiting for device"
device = MonkeyRunner.waitForConnection()
package = 'com.gamehivecorp.taptitans'
run_click("RUN", 0.025)
