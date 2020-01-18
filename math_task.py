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
import os.path as op
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

# Constants
OPERATOR_DICT = {'+': 'add', '-':'subtract', '/':'divide', '*':'multiply'}
TOTAL_DURATION = 450.
LEAD_IN_DURATION = 6.
END_SCREEN_DURATION = 2.
N_RUNS = 2

_INSTRUCTIONS = """\
You will be shown a series of formulae and individual numbers,
you must determine if the result is less than, equal to, or greater than
the value that follows:
      1 - Less Than
      2 - Equal to
      3 - Greater Than"""


if __name__ == '__main__':
    # Ensure that relative paths start from the same directory as this script
    try:
        script_dir = op.dirname(op.abspath(__file__)).decode(sys.getfilesystemencoding())
    except AttributeError:
        script_dir = op.dirname(op.abspath(__file__))

    # Collect user input
    # ------------------
    # Remember to turn fullscr to True for the real deal.
    all_config_files = sorted(glob(op.join(script_dir, 'config/sub*_config.tsv')))
    all_config_files = [op.basename(acf) for acf in all_config_files]
    all_subjects = sorted(list(set([acf.split('_')[0].split('-')[1] for acf in all_config_files])))
    all_sessions = sorted(list(set([acf.split('_')[1].split('-')[1] for acf in all_config_files])))
    exp_info = {'Subject': all_subjects,
                'Session': all_sessions,
                'BioPac': ['Yes', 'No']}

    dlg = gui.DlgFromDict(
        exp_info,
        title='Math task',
        order=['Subject', 'Session', 'BioPac'])
    window = visual.Window(
        # size=(800, 600), fullscr=True, monitor='testMonitor', units='norm',
        size=(500, 400), fullscr=False, monitor='testMonitor', units='norm',
        allowStencil=False, allowGUI=False, color='black', colorSpace='rgb',
        blendMode='avg', useFBO=True)
    if not dlg.OK:
        core.quit()  # user pressed cancel

    exp_info['date'] = data.getDateStr()  # add a simple timestamp
    exp_info['exp_name'] = 'math'

    if exp_info['BioPac'] == 'Yes':
        ser = serial.Serial('COM2', 115200)

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    base_name = 'sub-{0}_ses-{1}_task-math'.format(exp_info['Subject'], exp_info['Session'])

    for i_run in range(1, N_RUNS+1):
        config_file = op.join(script_dir, 'config',
                              '{0}_run-{1:02d}_config.tsv'.format(base_name, i_run))
        if not op.isfile(config_file):
            raise Exception('Config file not found: {}'.format(config_file))

    # save a log file for detail verbose info
    filename = op.join(script_dir, 'data/{0}_events'.format(base_name))
    logfile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    # An ExperimentHandler isn't essential but helps with data saving
    curr_exp = data.ExperimentHandler(name=exp_info['exp_name'], version='',
                                      extraInfo=exp_info, runtimeInfo=None,
                                      originPath=None,
                                      savePickle=True, saveWideText=True,
                                      dataFileName=filename)

    END_EXP_FLAG = False  # flag for 'escape' or other condition => quit the exp

    # store frame rate of monitor if we can measure it
    exp_info['frame_rate'] = window.getActualFrameRate()
    if not exp_info['frame_rate']:
        frame_duration = 1.0 / round(exp_info['frame_rate'])
    else:
        frame_duration = 1.0 / 60.0  # could not measure, so guess

    # Initialize stimuli
    # ------------------
    instruction_text_box = visual.TextStim(
        win=window,
        name='instruction_text_box',
        text=_INSTRUCTIONS,
        font=u'Arial',
        height=0.1,
        pos=(0, 0),
        wrapWidth=None,
        ori=0,
        color='white',
        colorSpace='rgb',
        opacity=1,
        depth=-1.0)
    lval_image = visual.ImageStim(
        win=window,
        name='equation_first_term',
        image=None,
        ori=0,
        pos=(-.3, 0),
        color=[1, 1, 1],
        colorSpace='rgb',
        opacity=1,
        depth=-1.0,
        interpolate=True)
    op_image = visual.ImageStim(
        win=window,
        name='equation_operator',
        image=None,
        ori=0,
        pos=(0, 0),
        color=[1, 1, 1],
        colorSpace='rgb',
        opacity=1,
        depth=-1.0,
        interpolate=True)
    rval_image = visual.ImageStim(
        win=window,
        name='equation_second_term',
        image=None,
        ori=0,
        pos=(.3, 0),
        color=[1, 1, 1],
        colorSpace='rgb',
        opacity=1,
        depth=-1.0,
        interpolate=True)
    eq_image = visual.ImageStim(
        win=window,
        name='equation',
        image=None,
        ori=0,
        pos=(0, 0),
        color=[1, 1, 1],
        colorSpace='rgb',
        opacity=1,
        depth=-1.0,
        interpolate=True)
    comparison_image = visual.ImageStim(
        win=window,
        name='comparison',
        image=None,
        ori=0,
        pos=(0, 0),
        color=[1, 1, 1],
        colorSpace='rgb',
        opacity=1,
        depth=-1.0,
        interpolate=True)
    feedback_image = visual.ImageStim(
        win=window,
        name='feedback',
        image=None,
        size=(0.25, 0.375),
        ori=0,
        pos=(0, 0),
        color=[1, 1, 1],
        colorSpace='rgb',
        opacity=1,
        depth=-1.0,
        interpolate=True)
    fixation_text = visual.TextStim(
        win=window,
        name='fixation',
        text=u'\u2022',
        font=u'Arial',
        pos=(0, 0),
        height=0.14,
        wrapWidth=None,
        ori=0,
        color='white',
        colorSpace='rgb',
        opacity=1,
        depth=0.0)

    # Scanner runtime
    # ---------------
    global_clock = core.Clock()  # to track the time since experiment started
    routine_timer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
    comparison_window_clock = core.Clock()
    pre_comparison_interval_clock = core.Clock()
    begin_fixClock = core.Clock()
    instructions_clock = core.Clock()
    equation_window_clock = core.Clock()
    post_comparison_interval_clock = core.Clock()
    feedback_window_clock = core.Clock()
    post_feedback_interval_clock = core.Clock()

    # set up handler to look after randomisation of conditions etc
    run_loop = data.TrialHandler(nReps=N_RUNS, method='random',
                                 extraInfo=exp_info, originPath=-1,
                                 trialList=[None],
                                 seed=None, name='run_loop')
    curr_exp.addLoop(run_loop)  # add the loop to the experiment
    curr_run = run_loop.trialList[0]  # so we can initialise stimuli with some values

    for curr_run in run_loop:
        run_data = {'onset':[], 'duration':[], 'trial_type':[],
                    'equation':[], 'feedback_type':[], 'comparison':[],
                    'response_time':[], 'accuracy':[], 'response': [],
                    'stim_file_operator': [], 'stim_file_feedback': [],
                    'stim_file_left': [], 'stim_file_right': [],
                    'stim_file_comparison': [],
                    'comparison_onset': [], 'comparison_duration': [],
                    'feedback_onset': [], 'feedback_duration': [],
                    'equation_representation': [], 'comparison_representation': []}
        currentLoop = run_loop
        run_label = run_loop.thisN + 1
        config_file = op.join(script_dir, 'config',
                              '{0}_run-{1:02d}_config.tsv'.format(base_name, run_label))
        config_df = pd.read_table(config_file)
        outfile = op.join(script_dir, 'data',
                           '{0}_run-{1:02d}_events.tsv'.format(base_name, run_label))

        # Reset BioPac
        if exp_info['BioPac'] == 'Yes':
            ser.write('RR')

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
                window.callOnFlip(instruction_end_resp.clock.reset)
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
                run_frame.to_csv(outfile, index=None, sep='\t')
                core.quit()

            # refresh the screen
            if CONTINUE_ROUTINE_FLAG:  # don't flip if this routine is over or we'll get a blank screen
                window.flip()

        # -------Ending Routine "instructions"-------
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # Start recording
        if exp_info['BioPac'] == 'Yes':
            ser.write('FF')

        startTime = datetime.now()

        # ------Prepare to start Routine "begin_fix"-------
        global_clock.reset()
        t = 0
        begin_fixClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routine_timer.reset()
        routine_timer.add(LEAD_IN_DURATION)
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
            frameRemains = LEAD_IN_DURATION - window.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_text.status == STARTED and t >= LEAD_IN_DURATION:
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
                run_frame.to_csv(outfile, index=None, sep='\t')
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                window.flip()

        # -------Ending Routine "begin_fix"-------
        for thisComponent in begin_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
        routine_timer.reset()

        # set up handler to look after randomisation of conditions etc
        trial_loop = data.TrialHandler(nReps=config_df.shape[0], method='random',
                                       extraInfo=exp_info, originPath=-1,
                                       trialList=[None],
                                       seed=None, name='trial_loop')
        curr_exp.addLoop(trial_loop)  # add the loop to the experiment
        curr_trial = trial_loop.trialList[0]  # so we can initialise stimuli with some values

        for curr_trial in trial_loop:
            # This section (before the "prepare" portion) takes ~0.4s with 300dpi images
            # Within reasonable range for 72dpi images
            currentLoop = trial_loop
            trial_num = trial_loop.thisN

            trial_type = config_df.loc[trial_num, 'trial_type']
            equation = config_df.loc[trial_num, 'equation']
            feedback_type = config_df.loc[trial_num, 'feedback']
            num_type_eq = config_df.loc[trial_num, 'equation_representation']
            num_type_comp = config_df.loc[trial_num, 'comparison_representation']
            comparison = int(config_df.loc[trial_num, 'comparison'])
            rounded_difference = int(config_df.loc[trial_num, 'rounded_difference'])
            solution = config_df.loc[trial_num, 'solution']

            if trial_type == 'math':
                operator = [x for x in equation if not x.isdigit()][0]
                lval, rval = equation.split(operator)
                lval_image.setImage(op.join(
                    script_dir,
                    'stimuli/numerals/{0:02d}_{1}.png'.format(int(lval), num_type_eq[0])))
                rval_image.setImage(op.join(
                    script_dir,
                    'stimuli/numerals/{0:02d}_{1}.png'.format(int(rval), num_type_eq[0])))
                if num_type_eq == 'numeric':
                    img_ratio = lval_image.size[0] / lval_image.size[1]
                    lval_image.size = [0.45 * img_ratio, 0.45]
                    img_ratio = rval_image.size[0] / rval_image.size[1]
                    rval_image.size = [0.45 * img_ratio, 0.45]
                    lval_image.pos = (-0.3, 0.0)
                    rval_image.pos = (0.3, 0.0)
                elif num_type_eq == 'word':
                    img_ratio = lval_image.size[0] / lval_image.size[1]
                    lval_image.size = [0.45 * img_ratio, 0.45]
                    img_ratio = rval_image.size[0] / rval_image.size[1]
                    rval_image.size = [0.45 * img_ratio, 0.45]
                    lval_image.pos = (0.0, 0.4)
                    rval_image.pos = (0.0, -0.4)
                elif num_type_eq == 'analog':  # unused
                    lval_image.size = (0.45, 0.675)
                    rval_image.size = (0.45, 0.675)
                    lval_image.pos = (-0.45, 0.0)
                    rval_image.pos = (0.45, 0.0)
                else:
                    raise Exception('num_type_eq must be "analog", "numeric", '
                                    'or "word", not {}'.format(num_type_eq))

                op_image.setImage(op.join(
                    script_dir,
                    'stimuli/numerals/{0}_{1}.png'.format(OPERATOR_DICT[operator], num_type_eq[0])))
                img_ratio = op_image.size[0] / op_image.size[1]
                op_image.size = [0.45 * img_ratio, 0.45]
            else:  # null trials- just memorize the number
                solution = int(equation)
                eq_image.setImage(op.join(
                    script_dir,
                    'stimuli/numerals/{0:02d}_{1}.png'.format(solution, num_type_eq[0])))
                img_ratio = eq_image.size[0] / eq_image.size[1]
                eq_image.size = [0.45 * img_ratio, 0.45]
                eq_image.pos = (0.0, 0.0)

            comparison_image.setImage(op.join(
                script_dir,
                'stimuli/numerals/{0:02d}_{1}.png'.format(comparison, num_type_comp[0])))
            img_ratio = comparison_image.size[0] / comparison_image.size[1]
            #print('START')
            #print(comparison_image.image)
            #print(comparison_image.size[0])
            #print(comparison_image.size[1])
            #print(img_ratio)
            #print(0.45 * img_ratio)
            #print('DONE')
            comparison_image.size = [0.45, 0.45 * img_ratio]
            comparison_image.pos = (0.0, 0.0)

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
            routine_timer.add(config_df.loc[trial_num, 'equation_duration'])
            # update component parameters for each repeat
            # keep track of which components have finished
            if trial_type == 'math':
                equation_windowComponents = [lval_image, op_image, rval_image]
            else:
                equation_windowComponents = [eq_image]

            for thisComponent in equation_windowComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "equation_window"-------
            while CONTINUE_ROUTINE_FLAG and routine_timer.getTime() > 0:
                # get current time
                t = equation_window_clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                if trial_type == 'math':
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

                    frameRemains = config_df.loc[trial_num, 'equation_duration'] - window.monitorFramePeriod * 0.75  # most of one frame period left
                    if lval_image.status == STARTED and t >= frameRemains:
                        lval_image.setAutoDraw(False)
                        op_image.setAutoDraw(False)
                        rval_image.setAutoDraw(False)
                else:
                    # *eq_image* updates
                    if t >= 0.0 and eq_image.status == NOT_STARTED:
                        equation_onset_time = global_clock.getTime()
                        # keep track of start time/frame for later
                        eq_image.tStart = t
                        eq_image.frameNStart = frameN  # exact frame index
                        eq_image.setAutoDraw(True)

                    frameRemains = config_df.loc[trial_num, 'equation_duration'] - window.monitorFramePeriod * 0.75  # most of one frame period left
                    if eq_image.status == STARTED and t >= frameRemains:
                        eq_image.setAutoDraw(False)

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
                    run_frame.to_csv(outfile, index=None, sep='\t')
                    core.quit()

                # refresh the screen
                if CONTINUE_ROUTINE_FLAG:# don't flip if routine is over
                    window.flip()

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
            routine_timer.add(config_df.loc[trial_num, 'isi1'])
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
                frameRemains = config_df.loc[trial_num, 'isi1'] - window.monitorFramePeriod * 0.75  # most of one frame period left
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
                    run_frame.to_csv(outfile, index=None, sep='\t')
                    core.quit()

                # refresh the screen
                if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                    window.flip()

            # -------Ending Routine "pre_comparison_interval"-------
            for thisComponent in pre_comparison_intervalComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

            # ------Prepare to start Routine "comparison_window"-------
            t = 0
            comparison_window_clock.reset()  # clock
            frameN = -1
            CONTINUE_ROUTINE_FLAG = True
            routine_timer.add(config_df.loc[trial_num, 'comparison_duration'])
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
                frameRemains = config_df.loc[trial_num, 'comparison_duration'] - window.monitorFramePeriod * 0.75  # most of one frame period left
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
                    run_frame.to_csv(outfile, index=None, sep='\t')
                    core.quit()

                # refresh the screen
                if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                    window.flip()

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
            routine_timer.add(config_df.loc[trial_num, 'isi2'])
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

                frameRemains = config_df.loc[trial_num, 'isi2'] - window.monitorFramePeriod * 0.75  # most of one frame period left
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
                    run_frame.to_csv(outfile, index=None, sep='\t')
                    core.quit()

                # refresh the screen
                if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                    window.flip()

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

            if feedback_type == 'noninformative':
                feedback_image.image = 'stimuli/feedback/noninformative.png'
            elif trial_status == 'correct':
                feedback_image.image = 'stimuli/feedback/positive.png'
            elif trial_status == 'incorrect':
                feedback_image.image = 'stimuli/feedback/negative.png'
            else:  # no response
                feedback_image.image = 'stimuli/feedback/negative.png'

            t = 0
            feedback_window_clock.reset()  # clock
            frameN = -1
            CONTINUE_ROUTINE_FLAG = True
            routine_timer.add(config_df.loc[trial_num, 'feedback_duration'])
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
                frameRemains = config_df.loc[trial_num, 'feedback_duration'] - window.monitorFramePeriod * 0.75  # most of one frame period left
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
                    run_frame.to_csv(outfile, index=None, sep='\t')
                    core.quit()

                # refresh the screen
                if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                    window.flip()

            # -------Ending Routine "feedback_window"-------
            for thisComponent in feedback_windowComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

            feedback_duration = global_clock.getTime() - feedback_onset_time
            # the Routine "feedback_window" was not non-slip safe, so reset the non-slip timer
            routine_timer.reset()
            run_data['onset'].append(equation_onset_time)
            run_data['duration'].append(equation_duration)
            run_data['trial_type'].append(trial_type)
            run_data['comparison_onset'].append(comparison_onset_time)
            run_data['comparison_duration'].append(comparison_duration)
            run_data['feedback_onset'].append(feedback_onset_time)
            run_data['feedback_duration'].append(feedback_duration)
            run_data['equation_representation'].append(num_type_eq)
            run_data['comparison_representation'].append(num_type_comp)
            run_data['response'].append(response_value)
            run_data['accuracy'].append(trial_status)
            run_data['response_time'].append(comparison_resp.rt if not isinstance(comparison_resp.rt, list) else 'n/a')
            run_data['equation'].append(equation)
            run_data['comparison'].append(comparison)
            run_data['feedback_type'].append(feedback_type)
            run_data['stim_file_left'].append(lval_image.image)
            run_data['stim_file_right'].append(rval_image.image)
            run_data['stim_file_operator'].append(op_image.image)
            run_data['stim_file_comparison'].append(comparison_image.image)
            run_data['stim_file_feedback'].append(feedback_image.image)

            # ------Prepare to start Routine "post_feedback_interval"-------
            t = 0
            post_feedback_interval_clock.reset()  # clock
            frameN = -1
            CONTINUE_ROUTINE_FLAG = True
            routine_timer.add(config_df.loc[trial_num, 'iti'])
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
                frameRemains = config_df.loc[trial_num, 'iti'] - window.monitorFramePeriod * 0.75  # most of one frame period left
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
                    run_frame.to_csv(outfile, sep='\t', line_terminator='\n', na_rep='n/a', index=False)
                    core.quit()

                # refresh the screen
                if CONTINUE_ROUTINE_FLAG:  # don't flip if routine is over
                    window.flip()

            # -------Ending Routine "post_feedback_interval"-------
            for thisComponent in post_feedback_intervalComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            curr_exp.nextEntry()

        # end trial_loop
        curr_exp.nextEntry()
        run_frame = pd.DataFrame(run_data)
        run_frame.to_csv(outfile, sep='\t', line_terminator='\n', na_rep='n/a', index=False)

        if exp_info['BioPac'] == 'Yes':
            ser.write('00')

        duration = datetime.now() - startTime
        print('Total duration of run: {}'.format(duration))
    # end run_loop

    # Shut down serial port connection
    if exp_info['BioPac'] == 'Yes':
        ser.close()

    # these shouldn't be strictly necessary (should auto-save)
    curr_exp.saveAsWideText(filename+'.csv')
    curr_exp.saveAsPickle(filename)
    logging.flush()

    # make sure everything is closed down
    curr_exp.abort()  # or data files will save again on exit
    window.close()
    core.quit()
