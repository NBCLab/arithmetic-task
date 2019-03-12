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
#pylint: disable=E0401,E1101,C0103
from __future__ import absolute_import, division
import os  # handy system and path functions
import sys  # to get file system encoding
import ast
from psychopy import gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, STOPPED, FINISHED)
import numpy as np  # whole numpy lib is available, prepend 'np.'

# Ensure that relative paths start from the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(script_dir)

# Store info about the experiment session
exp_name = u'math_task'  # from the Builder filename that created this script
exp_info = {u'operations': u"'+-*/'", u'participant': u'', u'scanner': u"''"}
dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)
if not dlg.OK:
    core.quit()  # user pressed cancel
exp_info['date'] = data.getDateStr()  # add a simple timestamp
exp_info['exp_name'] = exp_name

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = script_dir + os.sep + u'data/%s_%s_%s' % (exp_info['participant'],
                                                     exp_name,
                                                     exp_info['date'])

# An ExperimentHandler isn't essential but helps with data saving
this_experiment = data.ExperimentHandler(name=exp_name, version='',
                                         extraInfo=exp_info, runtimeInfo=None,
                                         originPath=None,
                                         savePickle=True, saveWideText=True,
                                         dataFileName=filename)
# save a log file for detail verbose info
log_file = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

END_EXP_FLAG = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
main_window = visual.Window(size=(1366, 768), fullscr=True, screen=0,
                            allowGUI=False, allowStencil=False,
                            monitor=u'testMonitor', color=[0, 0, 0],
                            colorSpace='rgb', blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
exp_info['frameRate'] = main_window.getActualFrameRate()
if exp_info['frameRate'] != None:
    frame_duration = 1.0 / round(exp_info['frameRate'])
else:
    frame_duration = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instruction_clock = core.Clock()
if exp_info['scanner']:
    INSTRUCTION_TEXT = \
    ' You will be shown a series of formulas, \
    \nyou must determine if the result is less than, equal to,  or greater than 5 \
    \n      1 - Less Than  2 - Equal to  3 - Greater Than'
else:
    INTRUSCTION_TEXT = \
    ' You will be shown a series of formulas, \
    \nyou must determine if the result is less than, equal to,  or greater than 5 \
    \n      1 - Less Than  2 - Equal to  3 - Greater Than'
MATH_TEXT = ''

INSTRUCTION_TEXT_BOX = visual.TextStim(win=main_window, name='INSTRUCTION_TEXT_BOX',
                                       text=INSTRUCTION_TEXT,
                                       font=u'Arial',
                                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                       color=u'white', colorSpace='rgb', opacity=1,
                                       depth=-1.0)

# Initialize components for Routine "trial"
trial_clock = core.Clock()
MATH_TEXT_BOX = visual.TextStim(win=main_window, name='MATH_TEXT_BOX',
                                text='default text',
                                font=u'Arial',
                                pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                color=u'white', colorSpace='rgb', opacity=1,
                                depth=0.0)

MATH_FIX = visual.Polygon(win=main_window, name='MATH_FIX',
                          edges=99, size=(0.1, 0.1),
                          ori=0, pos=(0, 0),
                          lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
                          fillColor=[1, 1, 1], fillColorSpace='rgb',
                          opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "feedback"
feedback_clock = core.Clock()
FEEDBACK_TEXT_BOX = visual.TextStim(win=main_window, name='FEEDBACK_TEXT_BOX',
                                    text='default text',
                                    font=u'Arial',
                                    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                    color=u'white', colorSpace='rgb', opacity=1,
                                    depth=0.0)
ISI = core.StaticPeriod(win=main_window, screenHz=exp_info['frameRate'], name='ISI')
FEEDBACK_TEXT = ''


# Create some handy timers
global_clock = core.Clock()  # to track the time since experiment started
routine_timer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "instructions"-------
t = 0
instruction_clock.reset()  # clock
frame_n = -1
CONTINUE_ROUTINE_FLAG = True
# update component parameters for each repeat

INSTRUCTION_END_RESP = event.BuilderKeyResponse()
# keep track of which components have finished
instruction_components = [INSTRUCTION_TEXT_BOX, INSTRUCTION_END_RESP]
for thisComponent in instruction_components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while CONTINUE_ROUTINE_FLAG:
    # get current time
    routine_time = instruction_clock.getTime()
    frame_n = frame_n + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *INSTRUCTION_TEXT_BOX* updates
    if routine_time >= 0.0 and INSTRUCTION_TEXT_BOX.status == NOT_STARTED:
        # keep track of start time/frame for later
        INSTRUCTION_TEXT_BOX.tStart = routine_time
        INSTRUCTION_TEXT_BOX.frameNStart = frame_n  # exact frame index
        INSTRUCTION_TEXT_BOX.setAutoDraw(True)

    # *INSTRUCTION_END_RESP* updates
    if routine_time >= 0.0 and INSTRUCTION_END_RESP.status == NOT_STARTED:
        # keep track of start time/frame for later
        INSTRUCTION_END_RESP.tStart = routine_time
        INSTRUCTION_END_RESP.frameNStart = frame_n  # exact frame index
        INSTRUCTION_END_RESP.status = STARTED
        # keyboard checking is just starting
        main_window.callOnFlip(INSTRUCTION_END_RESP.clock.reset)
        event.clearEvents(eventType='keyboard')
    if INSTRUCTION_END_RESP.status == STARTED:
        current_key_list = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in current_key_list:
            END_EXP_FLAG = True
        if current_key_list:  # at least one key was pressed
            INSTRUCTION_END_RESP.keys = current_key_list[-1]  # just the last key pressed
            INSTRUCTION_END_RESP.rt = INSTRUCTION_END_RESP.clock.getTime()
            # a response ends the routine
            CONTINUE_ROUTINE_FLAG = False

    # check if all components have finished
    if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
        break
    CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
    for thisComponent in instruction_components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            CONTINUE_ROUTINE_FLAG = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
        main_window.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instruction_components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if INSTRUCTION_END_RESP.keys in ['', [], None]:  # No response was made
    INSTRUCTION_END_RESP.keys = None
this_experiment.addData('INSTRUCTION_END_RESP.keys', INSTRUCTION_END_RESP.keys)
if INSTRUCTION_END_RESP.keys != None:  # we had a response
    this_experiment.addData('INSTRUCTION_END_RESP.rt', INSTRUCTION_END_RESP.rt)
this_experiment.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routine_timer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=99, method='random',
                           extraInfo=exp_info, originPath=-1,
                           trialList=[None],
                           seed=None, name='trials')
this_experiment.addLoop(trials)  # add the loop to the experiment
current_trial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = current_trial.rgb)
for current_trial in trials:
    currentLoop = trials
    # ------Prepare to start Routine "trial"-------
    trial_time = 0
    trial_clock.reset()  # clock
    frame_n = -1
    CONTINUE_ROUTINE_FLAG = True
    routine_timer.add(5.500000)
    # update component parameters for each repeat
    MATH_TEXT_BOX.setText(MATH_TEXT)
    MATH_TEXT_RESPONSE = event.BuilderKeyResponse()
    num_one = np.random.randint(0, 9)
    num_two = np.random.randint(0, 9)
    operator = exp_info['operations'][np.random.randint(0, len(exp_info['operations']))]

    MATH_TEXT = '{0} {1} {2}'.format(num_one, operator, num_two)
    MATH_VAL = ast.literal_eval(MATH_TEXT)
    if MATH_VAL < 5:
        MATH_CORR = '1'
    elif MATH_VAL == 5:
        MATH_CORR = '2'
    else:
        MATH_CORR = '3'


    # keep track of which components have finished
    trialComponents = [MATH_TEXT_BOX, MATH_TEXT_RESPONSE, MATH_FIX]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------
    while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
        # get current time
        trial_time = trial_clock.getTime()
        frame_n = frame_n + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *MATH_TEXT_BOX* updates
        if trial_time >= 0.0 and MATH_TEXT_BOX.status == NOT_STARTED:
            # keep track of start time/frame for later
            MATH_TEXT_BOX.tStart = trial_time
            MATH_TEXT_BOX.frameNStart = frame_n  # exact frame index
            MATH_TEXT_BOX.setAutoDraw(True)
        frameRemains = 0.0 + 5 - main_window.monitorFramePeriod * 0.75
        if MATH_TEXT_BOX.status == STARTED and trial_time >= frameRemains:
            MATH_TEXT_BOX.setAutoDraw(False)

        # *MATH_TEXT_RESPONSE* updates
        if trial_time >= 0.0 and MATH_TEXT_RESPONSE.status == NOT_STARTED:
            # keep track of start time/frame for later
            MATH_TEXT_RESPONSE.tStart = trial_time
            MATH_TEXT_RESPONSE.frameNStart = frame_n  # exact frame index
            MATH_TEXT_RESPONSE.status = STARTED
            # keyboard checking is just starting
            main_window.callOnFlip(MATH_TEXT_RESPONSE.clock.reset)
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 5- main_window.monitorFramePeriod * 0.75
        if MATH_TEXT_RESPONSE.status == STARTED and trial_time >= frameRemains:
            MATH_TEXT_RESPONSE.status = STOPPED
        if MATH_TEXT_RESPONSE.status == STARTED:
            current_key_list = event.getKeys(keyList=['1', '2', '3'])

            # check for quit:
            if "escape" in current_key_list:
                END_EXP_FLAG = True
            if current_key_list:  # at least one key was pressed
                MATH_TEXT_RESPONSE.keys = current_key_list[-1]  # just the last key pressed
                MATH_TEXT_RESPONSE.rt = MATH_TEXT_RESPONSE.clock.getTime()
                # was this 'correct'?
                if (MATH_TEXT_RESPONSE.keys == str(MATH_CORR)) \
                or (MATH_TEXT_RESPONSE.keys == MATH_CORR):
                    MATH_TEXT_RESPONSE.corr = 1
                else:
                    MATH_TEXT_RESPONSE.corr = 0
                # a response ends the routine
                CONTINUE_ROUTINE_FLAG = False


        # *MATH_FIX* updates
        if trial_time >= 5 and MATH_FIX.status == NOT_STARTED:
            # keep track of start time/frame for later
            MATH_FIX.tStart = trial_time
            MATH_FIX.frameNStart = frame_n  # exact frame index
            MATH_FIX.setAutoDraw(True)
        frameRemains = 5 + .5- main_window.monitorFramePeriod * 0.75
        if MATH_FIX.status == STARTED and trial_time >= frameRemains:
            MATH_FIX.setAutoDraw(False)

        # check if all components have finished
        if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
            break
        CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                CONTINUE_ROUTINE_FLAG = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
            main_window.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if MATH_TEXT_RESPONSE.keys in ['', [], None]:  # No response was made
        MATH_TEXT_RESPONSE.keys = None
        # was no response the correct answer?!
        if str(MATH_CORR).lower() == 'none':
            MATH_TEXT_RESPONSE.corr = 1  # correct non-response
        else:
            MATH_TEXT_RESPONSE.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('MATH_TEXT_RESPONSE.keys', MATH_TEXT_RESPONSE.keys)
    trials.addData('MATH_TEXT_RESPONSE.corr', MATH_TEXT_RESPONSE.corr)
    if MATH_TEXT_RESPONSE.keys != None:  # we had a response
        trials.addData('MATH_TEXT_RESPONSE.rt', MATH_TEXT_RESPONSE.rt)


    # ------Prepare to start Routine "feedback"-------
    routine_time = 0
    feedback_clock.reset()  # clock
    frame_n = -1
    CONTINUE_ROUTINE_FLAG = True
    routine_timer.add(6.000000)
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
    while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
        # get current time
        routine_time = feedback_clock.getTime()
        frame_n = frame_n + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *FEEDBACK_TEXT_BOX* updates
        if routine_time >= 0.0 and FEEDBACK_TEXT_BOX.status == NOT_STARTED:
            # keep track of start time/frame for later
            FEEDBACK_TEXT_BOX.tStart = routine_time
            FEEDBACK_TEXT_BOX.frameNStart = frame_n  # exact frame index
            FEEDBACK_TEXT_BOX.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- main_window.monitorFramePeriod * 0.75
        if FEEDBACK_TEXT_BOX.status == STARTED and routine_time >= frameRemains:
            FEEDBACK_TEXT_BOX.setAutoDraw(False)

        # *ISI* period
        if routine_time >= 1 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = routine_time
            ISI.frameNStart = frame_n  # exact frame index
            ISI.start(5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period

        # check if all components have finished
        if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
            break
        CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                CONTINUE_ROUTINE_FLAG = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
            main_window.flip()

    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    this_experiment.nextEntry()

# completed 99 repeats of 'trials'




# these shouldn't be strictly necessary (should auto-save)
this_experiment.saveAsWideText(filename+'.csv')
this_experiment.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
this_experiment.abort()  # or data files will save again on exit
main_window.close()
core.quit()
