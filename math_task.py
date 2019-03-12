#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on February 25, 2019, at 10:22
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'math_task'  # from the Builder filename that created this script
expInfo = {u'operations': u"'+-*/'", u'participant': u'', u'scanner': u"''"}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\Adam\\Documents\\GitHub\\math_task\\math_task.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
if expInfo['scanner']:
    INSTRUCTION_TEXT = \
    'You will be shown a series of formulas, \nyou must determine if the result is less than or greater than 5 \n      1 - Less Than  2 - Equal to  3 - Greater Than'
else:
    INTRUSCTION_TEXT = \
    'You will be shown a series of formulas, \nyou must determine if the result is less than or greater than 5 \n      1 - Less Than  2 - Equal to  3 - Greater Than'
MATH_TEXT = ''
print(expInfo['operations'])
INSTRUCTION_TEXT_BOX = visual.TextStim(win=win, name='INSTRUCTION_TEXT_BOX',
    text=INSTRUCTION_TEXT,
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
MATH_TEXT_BOX = visual.TextStim(win=win, name='MATH_TEXT_BOX',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

MATH_FIX = visual.Polygon(
    win=win, name='MATH_FIX',
    edges=99, size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
FEEDBACK_TEXT_BOX = visual.TextStim(win=win, name='FEEDBACK_TEXT_BOX',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
FEEDBACK_TEXT = ''


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

INSTRUCTION_END_RESP = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [INSTRUCTION_TEXT_BOX, INSTRUCTION_END_RESP]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *INSTRUCTION_TEXT_BOX* updates
    if t >= 0.0 and INSTRUCTION_TEXT_BOX.status == NOT_STARTED:
        # keep track of start time/frame for later
        INSTRUCTION_TEXT_BOX.tStart = t
        INSTRUCTION_TEXT_BOX.frameNStart = frameN  # exact frame index
        INSTRUCTION_TEXT_BOX.setAutoDraw(True)
    
    # *INSTRUCTION_END_RESP* updates
    if t >= 0.0 and INSTRUCTION_END_RESP.status == NOT_STARTED:
        # keep track of start time/frame for later
        INSTRUCTION_END_RESP.tStart = t
        INSTRUCTION_END_RESP.frameNStart = frameN  # exact frame index
        INSTRUCTION_END_RESP.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(INSTRUCTION_END_RESP.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if INSTRUCTION_END_RESP.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            INSTRUCTION_END_RESP.keys = theseKeys[-1]  # just the last key pressed
            INSTRUCTION_END_RESP.rt = INSTRUCTION_END_RESP.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if INSTRUCTION_END_RESP.keys in ['', [], None]:  # No response was made
    INSTRUCTION_END_RESP.keys=None
thisExp.addData('INSTRUCTION_END_RESP.keys',INSTRUCTION_END_RESP.keys)
if INSTRUCTION_END_RESP.keys != None:  # we had a response
    thisExp.addData('INSTRUCTION_END_RESP.rt', INSTRUCTION_END_RESP.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=99, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.500000)
    # update component parameters for each repeat
    MATH_TEXT_BOX.setText(MATH_TEXT
)
    MATH_TEXT_RESPONSE = event.BuilderKeyResponse()
    num_one = np.random.randint(0, 99)
    num_two = np.random.randint(0, 99)
    operator = expInfo['operations'][np.random.randint(0, len(expInfo['operations']))]
    
    MATH_TEXT = '{0} {1} {2}'.format(num_one, operator, num_two)
    
    if eval(MATH_TEXT) < 5:
        MATH_CORR = '1'
    elif eval(MATH_TEXT) == 5:
        MATH_CORR = '2'
    else:
        MATH_CORR = '3'
        
    
    # keep track of which components have finished
    trialComponents = [MATH_TEXT_BOX, MATH_TEXT_RESPONSE, MATH_FIX]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MATH_TEXT_BOX* updates
        if t >= 0.0 and MATH_TEXT_BOX.status == NOT_STARTED:
            # keep track of start time/frame for later
            MATH_TEXT_BOX.tStart = t
            MATH_TEXT_BOX.frameNStart = frameN  # exact frame index
            MATH_TEXT_BOX.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if MATH_TEXT_BOX.status == STARTED and t >= frameRemains:
            MATH_TEXT_BOX.setAutoDraw(False)
        
        # *MATH_TEXT_RESPONSE* updates
        if t >= 0.0 and MATH_TEXT_RESPONSE.status == NOT_STARTED:
            # keep track of start time/frame for later
            MATH_TEXT_RESPONSE.tStart = t
            MATH_TEXT_RESPONSE.frameNStart = frameN  # exact frame index
            MATH_TEXT_RESPONSE.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(MATH_TEXT_RESPONSE.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if MATH_TEXT_RESPONSE.status == STARTED and t >= frameRemains:
            MATH_TEXT_RESPONSE.status = STOPPED
        if MATH_TEXT_RESPONSE.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                MATH_TEXT_RESPONSE.keys = theseKeys[-1]  # just the last key pressed
                MATH_TEXT_RESPONSE.rt = MATH_TEXT_RESPONSE.clock.getTime()
                # was this 'correct'?
                if (MATH_TEXT_RESPONSE.keys == str(MATH_CORR)) or (MATH_TEXT_RESPONSE.keys == MATH_CORR):
                    MATH_TEXT_RESPONSE.corr = 1
                else:
                    MATH_TEXT_RESPONSE.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        
        # *MATH_FIX* updates
        if t >= 5 and MATH_FIX.status == NOT_STARTED:
            # keep track of start time/frame for later
            MATH_FIX.tStart = t
            MATH_FIX.frameNStart = frameN  # exact frame index
            MATH_FIX.setAutoDraw(True)
        frameRemains = 5 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if MATH_FIX.status == STARTED and t >= frameRemains:
            MATH_FIX.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if MATH_TEXT_RESPONSE.keys in ['', [], None]:  # No response was made
        MATH_TEXT_RESPONSE.keys=None
        # was no response the correct answer?!
        if str(MATH_CORR).lower() == 'none':
           MATH_TEXT_RESPONSE.corr = 1  # correct non-response
        else:
           MATH_TEXT_RESPONSE.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('MATH_TEXT_RESPONSE.keys',MATH_TEXT_RESPONSE.keys)
    trials.addData('MATH_TEXT_RESPONSE.corr', MATH_TEXT_RESPONSE.corr)
    if MATH_TEXT_RESPONSE.keys != None:  # we had a response
        trials.addData('MATH_TEXT_RESPONSE.rt', MATH_TEXT_RESPONSE.rt)
    
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    FEEDBACK_TEXT_BOX.setText(FEEDBACK_TEXT)
    print(MATH_TEXT_RESPONSE.corr)
    if MATH_TEXT_RESPONSE.corr:
        FEEDBACK_TEXT = 'Correct'
    else:
        FEEDBACK_TEXT = 'Incorrect'
    # keep track of which components have finished
    feedbackComponents = [FEEDBACK_TEXT_BOX, ISI]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FEEDBACK_TEXT_BOX* updates
        if t >= 0.0 and FEEDBACK_TEXT_BOX.status == NOT_STARTED:
            # keep track of start time/frame for later
            FEEDBACK_TEXT_BOX.tStart = t
            FEEDBACK_TEXT_BOX.frameNStart = frameN  # exact frame index
            FEEDBACK_TEXT_BOX.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if FEEDBACK_TEXT_BOX.status == STARTED and t >= frameRemains:
            FEEDBACK_TEXT_BOX.setAutoDraw(False)
        
        # *ISI* period
        if t >= 1 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 99 repeats of 'trials'




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
