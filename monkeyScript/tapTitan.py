from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from random import randint
import time 
import thread
import threading
import os

STATE_IDLE = 0
STATE_START_CLICK = 1
STATE_RUN_CLICK = 2
STATE_EXIT = 3

state = STATE_IDLE
pointer = [0, 800]
click_pointer = [0, 0]
delay = 0.05

skill = False
skill_names = ["Heavenly Strike", "Shadow Clone", "Critical Strike", "War Cay","Berserker Rage", "Hand of Midas"]
skills = [False,False,False,False,False,False]

tab = False
tab_names = ["Player Skills", "Heros", "Artifacts", "Diamons"]
tabs = [False,False,False,False]

resolution = [1080, 1920]

clear = lambda: os.system('cls')
exit = False

print "waiting for device"
device = MonkeyRunner.waitForConnection()
package = 'com.gamehivecorp.taptitans'

started = False

class clickThread (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
    	started = True
    	run_click();
        

def run_click():
	while not exit:
		if state==STATE_RUN_CLICK:
			device.touch(pointer[0], pointer[1], 'DOWN_AND_UP')
			time.sleep(delay)
		
		# SKILLS
		index = 0
		for skll in skills:
			if skll:
				device.touch((resolution[0]/(len(skill_names)*2))*(index*2 + 1), resolution[1]-resolution[1]/8, 'DOWN_AND_UP')
				time.sleep(delay)
			skills[index] = False
			index = index + 1

		# TABS
		index = 0
		for tb in tabs:
			if tb:
				device.touch((resolution[0]/(len(tab_names)*2))*(index*2 + 1), resolution[1]-resolution[1]/64, 'DOWN_AND_UP')
				time.sleep(delay)
			tabs[index] = False
			index = index + 1

def help():
	print "==============================================================================="
	print 'This is help...'
	print '\tCOMMAND\t\t DESCRIPTION'
	print '\tstart\t\t going to start the clicking loop'
	print '\tstop\t\t going to stop the clicking loop'
	print '\tpointer\t\t set pointer location (x and y are integer)'
	print '\tclick\t\t click the screen one time (x and y are integer)'
	print '\tdelay\t\t set the delay between clicks when start\n\t\t\t ( best for',delay,')'
	print '\tresolution\t set the screen solution for better experience\n\t\t\t ( def is',resolution[0],'x',resolution[1],')'
	print '\ttab x\t\t show tab x [x is 0-3]'
	# print '\tskill\t\t toggle click on skills that available and turn on'
	print '\tskill x\t\t use skill x [x is 0-5]'
	# print '\tclear\t\t clear the screen'
	print '\thelp\t\t show help'
	print '\texit\t\t exit the program'
	print "_______________________________________________________________________________"

help()
thread = clickThread()
thread.start()

while state!=STATE_EXIT:

	if state == STATE_START_CLICK:	
		print '\tTry to start'
		try:
			state = STATE_RUN_CLICK
			print '\tStarted'
		except:
			state = STATE_IDLE
			print '\tcannot start clicking'

	string = raw_input(">> ")

	if string == 'start':
		if state == STATE_RUN_CLICK or state == STATE_START_CLICK:
			print '\tAlready start'
		else:
			print '\tChanging state'
			state = STATE_START_CLICK
	elif string == 'stop':
		state = STATE_IDLE
	elif string == 'help':
		help()
	elif string == 'pointer':
		pointer[0] = input('\tx : ')
		pointer[1] = input('\ty : ')
	elif string == 'click':
		click_pointer[0] = input('\tx : ')
		click_pointer[1] = input('\ty : ')
		device.touch(click_pointer[0], click_pointer[1], 'DOWN_AND_UP')
	elif string == 'delay':
		delay = input('\tdelay : ')
	elif string.split(' ')[0]=='skill' and len(string.split(' ')) > 1 :
		skill = True
		strs = string.split(' ')
		index = int(strs[1])
		if index >= 0 and index <= 5:
			skills[index] = True
			print '\tUse',
			print skill_names[index]
			skills[index] = True
		else:
			print '\tindex out of lenght'
	elif string.split(' ')[0]=='tab' and len(string.split(' ')) > 1 :
		tab = True
		strs = string.split(' ')
		index = int(strs[1])
		if index >= 0 and index <= 3:
			tabs[index] = True
			print '\tShow tab',
			print tab_names[index]
		else:
			print '\tindex out of lenght'
	elif string == 'exit':
		state = STATE_EXIT
	else:
		print '\tUsing "help" to show all command'

exit = True
print "\tExiting"
