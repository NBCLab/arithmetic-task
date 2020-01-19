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
import time
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


def close_on_esc(win):
    """
    Closes window if escape is pressed
    """
    if 'escape' in event.getKeys():
        win.close()
        core.quit()


def draw(win, stim, duration, clock):
    """
    Draw stimulus for a given duration.

    Parameters
    ----------
    win : (visual.Window)
    stim : object with `.draw()` method or list of such objects
    duration : (numeric)
        duration in seconds to display the stimulus
    """
    # Use a busy loop instead of sleeping so we can exit early if need be.
    start_time = time.time()
    response = event.BuilderKeyResponse()
    response.tStart = start_time
    response.frameNStart = 0
    response.status = STARTED
    window.callOnFlip(response.clock.reset)
    event.clearEvents(eventType='keyboard')
    while time.time() - start_time < duration:
        if isinstance(stim, list):
            for s in stim:
                s.draw()
        else:
            stim.draw()
        keys = event.getKeys(keyList=['1', '2', '3'], timeStamped=clock)
        if keys:
            response.keys.extend(keys)
            response.rt.append(response.clock.getTime())
        close_on_esc(win)
        win.flip()
    response.status = STOPPED
    return response.keys, response.rt


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
    end_screen = visual.TextStim(
        window,
        'The task is now complete.',
        name='end_screen',
        color='white')

    # Scanner runtime
    # ---------------
    global_clock = core.Clock()  # to track the time since experiment started
    routine_timer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
    trial_clock = core.Clock()  # to track duration of each stage in each trial

    # set up handler to look after randomisation of conditions etc
    run_loop = data.TrialHandler(nReps=N_RUNS, method='random',
                                 extraInfo=exp_info, originPath=-1,
                                 trialList=[None],
                                 seed=None, name='run_loop')
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

        # Scanner runtime
        # ---------------
        # Wait for trigger from scanner.
        instruction_text_box.draw()
        window.flip()
        event.waitKeys(keyList=['5'])

        # Start recording
        if exp_info['BioPac'] == 'Yes':
            ser.write('FF')

        startTime = datetime.now()

        # Beginning fixation
        trial_clock.reset()
        draw(win=window, stim=fixation_text, duration=LEAD_IN_DURATION,
             clock=trial_clock)

        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
        routine_timer.reset()

        # set up handler to look after randomisation of conditions etc
        trial_loop = data.TrialHandler(nReps=config_df.shape[0], method='random',
                                       extraInfo=exp_info, originPath=-1,
                                       trialList=[None],
                                       seed=None, name='trial_loop')
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

            # Equation
            trial_clock.reset()
            equation_onset_time = global_clock.getTime()
            if trial_type == 'math':
                draw(win=window, stim=[lval_image, op_image, rval_image],
                     duration=config_df.loc[trial_num, 'equation_duration'],
                     clock=trial_clock)
            else:
                draw(win=window, stim=eq_image,
                     duration=config_df.loc[trial_num, 'equation_duration'],
                     clock=trial_clock)

            equation_duration = trial_clock.getTime()

            # the Routine "equation_window" was not non-slip safe, so reset the non-slip timer
            routine_timer.reset()

            # ISI1
            trial_clock.reset()
            isi1_keys, _ = draw(win=window, stim=fixation_text,
                                duration=config_df.loc[trial_num, 'isi1'],
                                clock=trial_clock)

            routine_timer.reset()

            # Comparison
            trial_clock.reset()
            comparison_onset_time = global_clock.getTime()
            task_keys, _ = draw(win=window, stim=comparison_image,
                                duration=config_df.loc[trial_num, 'comparison_duration'],
                                clock=trial_clock)
            comparison_duration = trial_clock.getTime()

            routine_timer.reset()

            # ISI2
            trial_clock.reset()
            isi2_keys, _ = draw(win=window, stim=fixation_text,
                                duration=config_df.loc[trial_num, 'isi2'],
                                clock=trial_clock)

            routine_timer.reset()

            # determine response
            if task_keys and isi2_keys:
                response_value = int(isi2_keys[-1][0])
                run_data['response_time'].append(task_keys[0][1])
            elif task_keys and not isi2_keys:
                response_value = int(task_keys[-1][0])
                run_data['response_time'].append(task_keys[0][1])
            elif isi2_keys and not task_keys:
                response_value = int(isi2_keys[-1][0])
                run_data['response_time'].append(isi2_keys[0][1])
            else:
                response_value = 'n/a'
                run_data['response_time'].append(np.nan)
            run_data['response'].append(response_value)

            # determine correct response
            if solution > comparison:
                corr_resp = 3
            elif solution == comparison:
                corr_resp = 2
            elif solution < comparison:
                corr_resp = 1

            # determine accuracy
            if response_value == 'n/a':
                trial_status = 'no_response'
            elif response_value == corr_resp:
                trial_status = 'correct'
            else:
                trial_status = 'incorrect'

            # determine feedback
            if feedback_type == 'noninformative':
                feedback_image.image = 'stimuli/feedback/noninformative.png'
            elif trial_status == 'correct':
                feedback_image.image = 'stimuli/feedback/positive.png'
            elif trial_status == 'incorrect':
                feedback_image.image = 'stimuli/feedback/negative.png'
            else:  # no response
                feedback_image.image = 'stimuli/feedback/negative.png'

            # feedback presentation
            trial_clock.reset()
            feedback_onset_time = global_clock.getTime()
            draw(win=window, stim=feedback_image,
                 duration=config_df.loc[trial_num, 'feedback_duration'],
                 clock=trial_clock)
            feedback_duration = trial_clock.getTime()

            routine_timer.reset()

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
            run_data['accuracy'].append(trial_status)
            run_data['equation'].append(equation)
            run_data['comparison'].append(comparison)
            run_data['feedback_type'].append(feedback_type)
            run_data['stim_file_left'].append(lval_image.image)
            run_data['stim_file_right'].append(rval_image.image)
            run_data['stim_file_operator'].append(op_image.image)
            run_data['stim_file_comparison'].append(comparison_image.image)
            run_data['stim_file_feedback'].append(feedback_image.image)

            # ITI
            trial_clock.reset()
            draw(win=window, stim=fixation_text,
                 duration=config_df.loc[trial_num, 'iti'],
                 clock=trial_clock)

            routine_timer.reset()

        # end trial_loop
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

    # Scanner is off for this
    trial_clock.reset()
    draw(win=window, stim=end_screen, duration=2, clock=trial_clock)

    logging.flush()

    # make sure everything is closed down
    window.close()
    core.quit()
