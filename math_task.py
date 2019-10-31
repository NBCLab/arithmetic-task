#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on June 26, 2019, at 17:43
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
#pylint: disable=E0401,E0611,C0103,W0611
from __future__ import absolute_import, division
import os  # handy system and path functions
import sys  # to get file system encoding
import json
import itertools as it
from glob import glob
from datetime import datetime
import pandas as pd
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle


# Ensure that relative paths start from the same directory as this script
try:
    script_dir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
except AttributeError:
    script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)

# Store info about the experiment session
exp_name = 'math'
exp_info = {'participant':'',
            'session':''}

OPERATOR_DICT = {'+': 'add', '-':'subtract', '/':'divide', '*':'multiply'}
LEAD_IN_TIME = 6
EQUATION_DURATION = 2.
COMPARISON_DURATION = 5.
FEEDBACK_DURATION = 2.
ISI1 = 0.5
ISI2 = 0.5
ITI = 0.5

dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)
if not dlg.OK:
    core.quit()  # user pressed cancel
exp_info['date'] = data.getDateStr()  # add a simple timestamp
exp_info['exp_name'] = exp_name
with open('config/subject_config.json') as fr:
    config_data = json.load(fr)

exp_info['participant'] = '{0:02d}'.format(int(exp_info['participant']))
exp_info['session'] = '{0:02d}'.format(int(exp_info['session']))

if exp_info['participant'] not in config_data:
    raise ValueError('Subject ID "{0}" not in config_data'.format(exp_info['participant']))

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = script_dir + os.sep + u'data/%s_%s_%s_%s' % (exp_info['participant'],
                                                        exp_info['session'],
                                                        exp_name,
                                                        exp_info['date'])

# An ExperimentHandler isn't essential but helps with data saving
curr_exp = data.ExperimentHandler(name=exp_name, version='',
                                  extraInfo=exp_info, runtimeInfo=None,
                                  originPath=None,
                                  savePickle=True, saveWideText=True,
                                  dataFileName=filename)
# save a log file for detail verbose info
log_file = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

END_EXP_FLAG = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    fullscr=True, size=(800, 600), monitor='testMonitor', units='norm',
    # fullscr=False, size=(800, 600), monitor='testMonitor', units='norm',
    allowGUI=False, allowStencil=False,
    color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
exp_info['frame_rate'] = win.getActualFrameRate()
if not exp_info['frame_rate']:
    frame_duration = 1.0 / round(exp_info['frame_rate'])
else:
    frame_duration = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructions_clock = core.Clock()
instruction_text = \
' You will be shown a series of formulas, \
\nyou must determine if the result is less than, equal to, greater than, \
\nthe value that follows \
\n      1 - Less Than  \
\n      2 - Equal to   \
\n      3 - Greater Than'
instruction_text_box = visual.TextStim(win=win, name='instruction_text_box',
                                       text=instruction_text,
                                       font=u'Arial',
                                       height=0.1,
                                       pos=(0, 0), wrapWidth=None, ori=0,
                                       color='white', colorSpace='rgb', opacity=1,
                                       depth=-1.0)

# Initialize components for Routine "equation_window"
equation_window_clock = core.Clock()
lval_image = visual.ImageStim(win=win, name='lval_image',
                              image=None,
                              size=(0.3, 0.45),
                              ori=0, pos=(-.3, 0),
                              color=[1, 1, 1],
                              colorSpace='rgb',
                              opacity=1, depth=-1.0, interpolate=True)
op_image = visual.ImageStim(win=win, name='op_image',
                            image=None,
                            size=(0.25, 0.375),
                            ori=0, pos=(0, 0),
                            color=[1, 1, 1],
                            colorSpace='rgb',
                            opacity=1, depth=-1.0, interpolate=True)
rval_image = visual.ImageStim(win=win, name='rval_image',
                              image=None,
                              size=(0.3, 0.45),
                              ori=0, pos=(.3, 0),
                              color=[1, 1, 1],
                              colorSpace='rgb',
                              opacity=1, depth=-1.0, interpolate=True)
feedback_image = visual.ImageStim(win=win, name='feedback_image',
                                  image=None,
                                  size=(0.25, 0.375),
                                  ori=0, pos=(0, 0),
                                  color=[1, 1, 1],
                                  colorSpace='rgb',
                                  opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "pre_comparison_interval"
pre_comparison_interval_clock = core.Clock()
begin_fixClock = core.Clock()
fixation_text = visual.TextStim(win=win, name='operator_text',
                                text=u'\u2022', font=u'Arial',
                                pos=(0, 0), height=0.14,
                                wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb',
                                opacity=1, depth=0.0)

# Initialize components for Routine "comparison_window"
comparison_window_clock = core.Clock()
comparison_image = visual.ImageStim(win=win, name='r3_image',
                                    image=None,
                                    size=(0.25, 0.375),
                                    ori=0, pos=(0, 0),
                                    color=[1, 1, 1],
                                    colorSpace='rgb',
                                    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "post_comparison_interval"
post_comparison_interval_clock = core.Clock()

# Initialize components for Routine "feedback_window"
feedback_window_clock = core.Clock()

# Initialize components for Routine "post_feedback_interval"
post_feedback_interval_clock = core.Clock()

# Create some handy timers
global_clock = core.Clock()  # to track the time since experiment started
routine_timer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
n_runs = len(config_data[exp_info['participant']][exp_info['session']])
# set up handler to look after randomisation of conditions etc
run_loop = data.TrialHandler(nReps=n_runs, method='random',
                             extraInfo=exp_info, originPath=-1,
                             trialList=[None],
                             seed=None, name='run_loop')
curr_exp.addLoop(run_loop)  # add the loop to the experiment
curr_run = run_loop.trialList[0]  # so we can initialise stimuli with some values

startTime = datetime.now()

for curr_run in run_loop:
    run_data = {'onset':[], 'duration':[], 'trial_type':[],
                'equation':[], 'feedback_type':[], 'comparison':[],
                'response_time':[], 'accuracy':[], 'response': [],
                'stimfile_operator': [], 'stimfile_feedback': [],
                'stimfile_left': [], 'stimfile_right': [],
                'comparison_onset': [], 'comparison_duration': [],
                'feedback_onset': [], 'feedback_duration': []}
    currentLoop = run_loop
    # abbreviate parameter names if possible (e.g. rgb = curr_run.rgb)
    run_label = run_loop.thisN + 1
    out_file = 'data/sub-{0}_ses-{1}_task-math_run-{2:02d}.tsv'.format(
        exp_info['participant'], exp_info['session'], run_label)
    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructions_clock.reset()  # clock
    frameN = -1
    CONTINUE_ROUTINE_FLAG = True
    # update component parameters for each repeat
    instruction_end_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructionsComponents = [instruction_text_box, instruction_end_resp]
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "instructions"-------
    while CONTINUE_ROUTINE_FLAG:
        # get current time
        t = instructions_clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *INSTRUCTION_TEXT_BOX* updates
        if t >= 0.0 and instruction_text_box.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruction_text_box.tStart = t
            instruction_text_box.frameNStart = frameN  # exact frame index
            instruction_text_box.setAutoDraw(True)

        # *INSTRUCTION_END_RESP* updates
        if t >= 0.0 and instruction_end_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruction_end_resp.tStart = t
            instruction_end_resp.frameNStart = frameN  # exact frame index
            instruction_end_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instruction_end_resp.clock.reset)
            event.clearEvents(eventType='keyboard')

        if instruction_end_resp.status == STARTED:
            current_key_list = event.getKeys(keyList=['5'])

            # check for quit:
            if "escape" in current_key_list:
                END_EXP_FLAG = True
            if current_key_list:  # at least one key was pressed
                instruction_end_resp.keys = current_key_list[-1]  # just the last key pressed
                instruction_end_resp.rt = instruction_end_resp.clock.getTime()
                # a response ends the routine
                CONTINUE_ROUTINE_FLAG = False
        # check if all components have finished
        if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
            break
        CONTINUE_ROUTINE_FLAG = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                CONTINUE_ROUTINE_FLAG = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
            run_frame = pd.DataFrame(run_data)
            run_frame.to_csv(out_file, index=None, sep='\t')
            core.quit()

        # refresh the screen
        if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "begin_fix"-------
    global_clock.reset()
    t = 0
    begin_fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routine_timer.reset()
    routine_timer.add(LEAD_IN_TIME)
    # update component parameters for each repeat
    # keep track of which components have finished
    begin_fixComponents = [fixation_text]
    for thisComponent in begin_fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "begin_fix"-------
    while continueRoutine:# and routine_timer.getTime() > 0:
        # get current time
        t = begin_fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *fixation_text* updates
        if t >= 0.0 and fixation_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_text.tStart = t
            fixation_text.frameNStart = frameN  # exact frame index
            fixation_text.setAutoDraw(True)
        frameRemains = LEAD_IN_TIME - win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_text.status == STARTED and t >= LEAD_IN_TIME:
            fixation_text.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in begin_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
            run_frame = pd.DataFrame(run_data)
            run_frame.to_csv(out_file, index=None, sep='\t')
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "begin_fix"-------
    for thisComponent in begin_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routine_timer.reset()
    n_trials = len(config_data[exp_info['participant']][exp_info['session']][str(run_label)])

    # set up handler to look after randomisation of conditions etc
    trial_loop = data.TrialHandler(nReps=n_trials, method='random',
                                   extraInfo=exp_info, originPath=-1,
                                   trialList=[None],
                                   seed=None, name='trial_loop')
    curr_exp.addLoop(trial_loop)  # add the loop to the experiment
    curr_trial = trial_loop.trialList[0]  # so we can initialise stimuli with some values

    for curr_trial in trial_loop:
        # This section (before the "prepare" portion) takes ~0.4s with 300dpi images
        # Within reasonable range for 72dpi images
        currentLoop = trial_loop
        trial_label = trial_loop.thisN

        trial_config = config_data[exp_info['participant']][exp_info['session']][str(run_label)][trial_label]
        equation = trial_config['equation']
        feedback = trial_config['feedback']
        num_type = trial_config['representation']
        comparison = int(trial_config['comparison'])
        rounded_difference = int(trial_config['rounded_difference'])
        solution = trial_config['solution']

        operator = [x for x in equation if not x.isdigit()][0]
        lval, rval = equation.split(operator)
        lval_image.setImage(r'numerals/{0:02d}{1}.png'.format(int(lval), num_type[0]))
        rval_image.setImage(r'numerals/{0:02d}{1}.png'.format(int(rval), num_type[0]))
        if num_type == 'analog':
            lval_image.size = (0.45, 0.675)
            rval_image.size = (0.45, 0.675)
            lval_image.pos = (-0.45, 0.0)
            rval_image.pos = (0.45, 0.0)
        elif num_type == 'numeric':
            lval_image.size = (0.3, 0.45)
            rval_image.size = (0.3, 0.45)
            lval_image.pos = (-0.3, 0.0)
            rval_image.pos = (0.3, 0.0)
        else:
            raise Exception()
        op_image.setImage(r'numerals/{0}.png'.format(OPERATOR_DICT[operator]))
        comparison_image.setImage(r'numerals/{0:02d}n.png'.format(comparison))
        if solution > comparison:
            corr_resp = 3
        elif solution == comparison:
            corr_resp = 2
        elif solution < comparison:
            corr_resp = 1

        # ------Prepare to start Routine "equation_window"-------
        t = 0
        equation_window_clock.reset()  # clock
        frameN = -1
        CONTINUE_ROUTINE_FLAG = True
        routine_timer.reset()
        routine_timer.add(EQUATION_DURATION)
        # update component parameters for each repeat
        # keep track of which components have finished
        equation_windowComponents = [lval_image, op_image, rval_image]
        for thisComponent in equation_windowComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "equation_window"-------
        while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
            # get current time
            t = equation_window_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *lval_image* updates
            if t >= 0.0 and lval_image.status == NOT_STARTED:
                equation_onset_time = global_clock.getTime()
                # keep track of start time/frame for later
                lval_image.tStart = t
                lval_image.frameNStart = frameN  # exact frame index
                lval_image.setAutoDraw(True)
                # keep track of start time/frame for later
                op_image.tStart = t
                op_image.frameNStart = frameN  # exact frame index
                op_image.setAutoDraw(True)
                # keep track of start time/frame for later
                rval_image.tStart = t
                rval_image.frameNStart = frameN  # exact frame index
                rval_image.setAutoDraw(True)

            frameRemains = EQUATION_DURATION - win.monitorFramePeriod * 0.75  # most of one frame period left
            if lval_image.status == STARTED and t >= frameRemains:
                lval_image.setAutoDraw(False)
                op_image.setAutoDraw(False)
                rval_image.setAutoDraw(False)

            # check if all components have finished
            if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
                break
            CONTINUE_ROUTINE_FLAG = False  #At least one component still running
            for thisComponent in equation_windowComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    CONTINUE_ROUTINE_FLAG = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
                run_frame = pd.DataFrame(run_data)
                run_frame.to_csv(out_file, index=None, sep='\t')
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:# don't flip if routine is over
                win.flip()

        # -------Ending Routine "equation_window"-------
        for thisComponent in equation_windowComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "equation_window" was not non-slip safe, so reset the non-slip timer
        routine_timer.reset()

        equation_duration = global_clock.getTime() - equation_onset_time

        # ------Prepare to start Routine "pre_comparison_interval"-------
        t = 0
        pre_comparison_interval_clock.reset()  # clock
        frameN = -1
        CONTINUE_ROUTINE_FLAG = True
        routine_timer.add(ISI1)
        # update component parameters for each repeat
        # keep track of which components have finished
        pre_comparison_intervalComponents = [fixation_text]
        for thisComponent in pre_comparison_intervalComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "pre_comparison_interval"-------
        while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
            # get current time
            t = pre_comparison_interval_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixation_text* updates
            if t >= 0.0 and fixation_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_text.tStart = t
                fixation_text.frameNStart = frameN  # exact frame index
                fixation_text.setAutoDraw(True)
            frameRemains = ISI1 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_text.status == STARTED and t >= frameRemains:
                fixation_text.setAutoDraw(False)

            # check if all components have finished
            if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
                break
            CONTINUE_ROUTINE_FLAG = False  #at least one component still running
            for thisComponent in pre_comparison_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    CONTINUE_ROUTINE_FLAG = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
                run_frame = pd.DataFrame(run_data)
                run_frame.to_csv(out_file, index=None, sep='\t')
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                win.flip()

        # -------Ending Routine "pre_comparison_interval"-------
        for thisComponent in pre_comparison_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # ------Prepare to start Routine "comparison_window"-------
        t = 0
        comparison_window_clock.reset()  # clock
        frameN = -1
        CONTINUE_ROUTINE_FLAG = True
        routine_timer.add(COMPARISON_DURATION)
        comparison_resp = event.BuilderKeyResponse()
        # update component parameters for each repeat
        # keep track of which components have finished
        comparison_windowComponents = [comparison_image, comparison_resp]
        for thisComponent in comparison_windowComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "comparison_window"-------
        while CONTINUE_ROUTINE_FLAG:
            # get current time
            t = comparison_window_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
                        # *lval_image* updates
            if t >= 0.0 and comparison_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                comparison_image.tStart = t
                comparison_image.frameNStart = frameN  # exact frame index
                comparison_image.setAutoDraw(True)
                comparison_onset_time = global_clock.getTime()
            frameRemains = COMPARISON_DURATION - win.monitorFramePeriod * 0.75  # most of one frame period left
            if comparison_image.status == STARTED and t >= frameRemains:
                comparison_image.setAutoDraw(False)
            if t >= 0.0 and comparison_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                comparison_resp.tStart = t  # underestimates by a little under one frame
                comparison_resp.frameNStart = frameN  # exact frame index
                comparison_resp.status = STARTED
                # keyboard checking is just starting
                comparison_resp.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if comparison_resp.status == STARTED and t >= frameRemains:
                comparison_resp.status = STOPPED

            if comparison_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3'])

                # check for quit:
                if "escape" in theseKeys:
                    END_EXP_FLAG = True
                if theseKeys:  # at least one key was pressed
                    comparison_resp.keys = int(theseKeys[-1])  # just the last key pressed
                    comparison_resp.rt = comparison_resp.clock.getTime()
                    # a response ends the routine
                    #continueRoutine = False

            # check if all components have finished
            if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
                break
            CONTINUE_ROUTINE_FLAG = False #at least one component still running
            for thisComponent in comparison_windowComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    CONTINUE_ROUTINE_FLAG = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
                run_frame = pd.DataFrame(run_data)
                run_frame.to_csv(out_file, index=None, sep='\t')
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                win.flip()

        # -------Ending Routine "comparison_window"-------
        for thisComponent in comparison_windowComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "comparison_window" was not non-slip safe, so reset the non-slip timer
        routine_timer.reset()

        comparison_duration = global_clock.getTime() - comparison_onset_time

        # ------Prepare to start Routine "post_comparison_interval"-------
        t = 0
        post_comparison_interval_clock.reset()  # clock
        frameN = -1
        CONTINUE_ROUTINE_FLAG = True
        routine_timer.add(ISI2)
        # update component parameters for each repeat
        # keep track of which components have finished
        post_comparison_intervalComponents = [fixation_text]
        for thisComponent in post_comparison_intervalComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "post_comparison_interval"-------
        while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
            # get current time
            t = post_comparison_interval_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixation_text* updates
            if t >= 0.0 and fixation_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_text.tStart = t
                fixation_text.frameNStart = frameN  # exact frame index
                fixation_text.setAutoDraw(True)

            frameRemains = ISI2 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_text.status == STARTED and t >= frameRemains:
                fixation_text.setAutoDraw(False)

            # check if all components have finished
            if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
                break

            CONTINUE_ROUTINE_FLAG = False  #at least one component still running
            for thisComponent in post_comparison_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    CONTINUE_ROUTINE_FLAG = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
                run_frame = pd.DataFrame(run_data)
                run_frame.to_csv(out_file, index=None, sep='\t')
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                win.flip()

        # -------Ending Routine "post_comparison_interval"-------
        for thisComponent in post_comparison_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # ------Prepare to start Routine "feedback_window"-------
        if isinstance(comparison_resp.keys, list):
            trial_status = 'no_response'
            response_value = 'n/a'
        elif comparison_resp.keys == corr_resp:
            trial_status = 'correct'
            response_value = comparison_resp.keys
        else:
            trial_status = 'incorrect'
            response_value = comparison_resp.keys

        if feedback == 'noninformative':
            feedback_image.image = 'feedback/noninformative.png'
        elif trial_status == 'correct':
            feedback_image.image = 'feedback/positive.png'
        elif trial_status == 'incorrect':
            feedback_image.image = 'feedback/negative.png'
        else:
            feedback_image.image = 'feedback/negative.png'

        t = 0
        feedback_window_clock.reset()  # clock
        frameN = -1
        CONTINUE_ROUTINE_FLAG = True
        routine_timer.add(FEEDBACK_DURATION)
        # update component parameters for each repeat
        # keep track of which components have finished
        feedback_windowComponents = [feedback_image]
        for thisComponent in feedback_windowComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "feedback_window"-------
        while CONTINUE_ROUTINE_FLAG:
            # get current time
            t = feedback_window_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if t >= 0.0 and feedback_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_image.tStart = t
                feedback_image.frameNStart = frameN  # exact frame index
                feedback_image.setAutoDraw(True)
                feedback_onset_time = global_clock.getTime()
            frameRemains = FEEDBACK_DURATION - win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedback_image.status == STARTED and t >= frameRemains:
                feedback_image.setAutoDraw(False)
            # check if all components have finished
            if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
                break
            CONTINUE_ROUTINE_FLAG = False  #at least one component still running
            for thisComponent in feedback_windowComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    CONTINUE_ROUTINE_FLAG = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
                run_frame = pd.DataFrame(run_data)
                run_frame.to_csv(out_file, index=None, sep='\t')
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                win.flip()

        # -------Ending Routine "feedback_window"-------
        for thisComponent in feedback_windowComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        feedback_duration = global_clock.getTime() - feedback_onset_time
        # the Routine "feedback_window" was not non-slip safe, so reset the non-slip timer
        routine_timer.reset()
        run_data['onset'].append(equation_onset_time)
        run_data['duration'].append(equation_duration)
        run_data['trial_type'].append(num_type)
        run_data['response_time'].append(comparison_resp.rt if not isinstance(comparison_resp.rt, list) else 'n/a')
        run_data['equation'].append(equation)
        run_data['feedback_type'].append(feedback)
        run_data['comparison'].append(comparison)
        run_data['accuracy'].append(trial_status)
        run_data['response'].append(response_value)
        run_data['stimfile_left'].append(lval_image.image)
        run_data['stimfile_right'].append(rval_image.image)
        run_data['stimfile_operator'].append(op_image.image)
        run_data['stimfile_feedback'].append(feedback_image.image)
        run_data['comparison_onset'].append(comparison_onset_time)
        run_data['comparison_duration'].append(comparison_duration)
        run_data['feedback_onset'].append(feedback_onset_time)
        run_data['feedback_duration'].append(feedback_duration)

        # ------Prepare to start Routine "post_feedback_interval"-------
        t = 0
        post_feedback_interval_clock.reset()  # clock
        frameN = -1
        CONTINUE_ROUTINE_FLAG = True
        routine_timer.add(ITI)
        # update component parameters for each repeat
        # keep track of which components have finished
        post_feedback_intervalComponents = [fixation_text]
        for thisComponent in post_feedback_intervalComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "post_feedback_interval"-------
        while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
            # get current time
            t = post_feedback_interval_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixation_text* updates
            if t >= 0.0 and fixation_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_text.tStart = t
                fixation_text.frameNStart = frameN  # exact frame index
                fixation_text.setAutoDraw(True)
            frameRemains = ITI - win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_text.status == STARTED and t >= frameRemains:
                fixation_text.setAutoDraw(False)

            # check if all components have finished
            if not CONTINUE_ROUTINE_FLAG:  # a component has requested a forced-end of Routine
                break
            CONTINUE_ROUTINE_FLAG = False  # at least one component still running
            for thisComponent in post_feedback_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    CONTINUE_ROUTINE_FLAG = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if END_EXP_FLAG or event.getKeys(keyList=["escape"]):
                run_frame = pd.DataFrame(run_data)
                run_frame.to_csv(out_file, index=None, sep='\t')
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                win.flip()

        # -------Ending Routine "post_feedback_interval"-------
        for thisComponent in post_feedback_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        curr_exp.nextEntry()

    # completed 5 repeats of 'trial_loop'
    curr_exp.nextEntry()
    run_frame = pd.DataFrame(run_data)
    run_frame.to_csv(out_file, index=None, sep='\t')
# completed 5 repeats of 'run_loop'

# these shouldn't be strictly necessary (should auto-save)
curr_exp.saveAsWideText(filename+'.csv')
curr_exp.saveAsPickle(filename)
logging.flush()

duration = datetime.now() - startTime
print('Total duration of task: {}'.format(duration))

# make sure everything is closed down
curr_exp.abort()  # or data files will save again on exit
win.close()
core.quit()
