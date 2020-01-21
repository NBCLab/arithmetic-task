from __future__ import absolute_import, division, print_function
import sys
import time
import serial
import os.path as op
from glob import glob

import numpy as np
import pandas as pd

from psychopy import gui, visual, core, data, event, logging
from psychopy.constants import STARTED, STOPPED


def set_word_size(img):
    # det from orig height 2row / orig height 1row
    const = 1.764505119453925

    # desired 1row height
    height_1row = 0.225
    height_2rows = height_1row * const
    width, height = img.size
    if height > 1:  # det by stim gen procedure
        new_height = height_2rows
    else:
        new_height = height_1row
    new_shape = (new_height * (width / height), new_height)
    return new_shape


def close_on_esc(win):
    """
    Closes window if escape is pressed
    """
    if 'escape' in event.getKeys():
        win.close()
        core.quit()


def draw(win, stim, keyList=['1', '2', '3']):
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
    while True:
        if isinstance(stim, list):
            for s in stim:
                s.draw()
        else:
            stim.draw()
        keys = event.getKeys(keyList=keyList)
        if keys:
            response.keys.extend(keys)
            break
        close_on_esc(win)
        win.flip()
    response.status = STOPPED
    return response.keys[0]


if __name__ == '__main__':
    # Ensure that relative paths start from the same directory as this script
    try:
        script_dir = op.dirname(op.abspath(__file__)).decode(sys.getfilesystemencoding())
    except AttributeError:
        script_dir = op.dirname(op.abspath(__file__))

    exp_info = {}

    dlg = gui.DlgFromDict(
        exp_info,
        title='Math task training')
    window = visual.Window(
        fullscr=False,
        size=(800, 600),
        monitor='testMonitor',
        units='norm',
        allowStencil=False,
        allowGUI=False,
        color='black',
        colorSpace='rgb',
        blendMode='avg',
        useFBO=True)
    if not dlg.OK:
        core.quit()  # user pressed cancel

    instruction_text_box = visual.TextStim(
        win=window,
        name='instruction_text_box',
        text="""\
You will be shown a series of formulae and individual numbers,
you must determine if the result is less than, equal to, or greater than
the value that follows:
      1 - Less Than
      2 - Equal to
      3 - Greater Than""",
        font=u'Arial',
        height=0.1,
        pos=(0, 0),
        wrapWidth=None,
        ori=0,
        color='white',
        colorSpace='rgb',
        opacity=1,
        depth=-1.0)
    term1_image = visual.ImageStim(
        win=window,
        name='equation_first_term',
        image=None,
        ori=0,
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
    term2_image = visual.ImageStim(
        win=window,
        name='equation_second_term',
        image=None,
        ori=0,
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
        size=None,
        ori=0,
        pos=(0, 0),
        color=[1, 1, 1],
        colorSpace='rgb',
        opacity=1,
        depth=-1.0,
        interpolate=True)

    instruction_text_box.draw()
    window.flip()
    event.waitKeys(keyList=['space'])

    instruction_text_box.setText('Each trial consists of three stages: an equation, a comparison value, and feedback.')
    instruction_text_box.draw()
    window.flip()
    event.waitKeys(keyList=['space'])

    instruction_text_box.setText('Your job is to solve the equation, and then compare the result to the comparison value.')
    instruction_text_box.draw()
    window.flip()
    event.waitKeys(keyList=['space'])

    instruction_text_box.setText("""If the solution is less than the comparison value, press 1 (index).
If it is equal to the comparison value, press 2 (middle).
If it is greater than, press 3 (ring)""")
    instruction_text_box.draw()
    window.flip()
    event.waitKeys(keyList=['space'])

    instruction_text_box.setText("Let's try practicing.")
    instruction_text_box.draw()
    window.flip()
    event.waitKeys(keyList=['space'])

    # First example- equation with numbers
    term1_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/10_n.png'))
    term2_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/01_n.png'))
    op_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/add_n.png'))
    comparison_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/10_n.png'))
    feedback_image.setImage(op.join(
        script_dir,
        'stimuli/feedback/positive.png'))

    term1_image.setSize(set_word_size(term1_image))
    term2_image.setSize(set_word_size(term2_image))
    op_image.setSize(set_word_size(op_image))
    comparison_image.setSize(set_word_size(comparison_image))
    width, height = feedback_image.size
    new_height = 0.6
    new_shape = (new_height * (width / height), new_height)
    feedback_image.setSize(new_shape)

    term1_pos = (term1_image.size[0] / 2.) + (op_image.size[0] / 2.)
    term2_pos = -1 * ((term2_image.size[0] / 2.) + (op_image.size[0] / 2.))
    term1_image.pos = (term1_pos, 0.0)
    term2_image.pos = (term2_pos, 0.0)

    draw(win=window, stim=[term1_image, op_image, term2_image], keyList=['space'])
    draw(win=window, stim=comparison_image, keyList=['3'])
    draw(win=window, stim=feedback_image, keyList=['space'])

    # Unset stim sizes so they don't pass on to the next trial
    term1_image.size = None
    op_image.size = None
    term2_image.size = None
    eq_image.size = None
    comparison_image.size = None

    # Instructions
    instruction_text_box.setText("""\
            Great job!

Now let's try an equation with
              words.""")
    draw(win=window, stim=instruction_text_box, keyList=['space'])

    # Next example- equation with words
    term1_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/05_w.png'))
    term2_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/07_w.png'))
    op_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/subtract_w.png'))
    comparison_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/-2_w.png'))
    feedback_image.setImage(op.join(
        script_dir,
        'stimuli/feedback/positive.png'))
    term1_image.setSize(set_word_size(term1_image))
    term2_image.setSize(set_word_size(term2_image))
    op_image.setSize(set_word_size(op_image))
    term1_pos = (term1_image.size[1] / 2.) + (op_image.size[1] / 2.)
    term2_pos = -1 * ((term2_image.size[1] / 2.) + (op_image.size[1] / 2.))
    term1_image.pos = (0.0, term1_pos)
    term2_image.pos = (0.0, term2_pos)

    comparison_image.setSize(set_word_size(comparison_image))
    width, height = feedback_image.size
    new_height = 0.6
    new_shape = (new_height * (width / height), new_height)
    feedback_image.setSize(new_shape)

    draw(win=window, stim=[term1_image, op_image, term2_image], keyList=['space'])
    draw(win=window, stim=comparison_image, keyList=['2'])
    draw(win=window, stim=feedback_image, keyList=['space'])

    # Unset stim sizes so they don't pass on to the next trial
    term1_image.size = None
    op_image.size = None
    term2_image.size = None
    eq_image.size = None
    comparison_image.size = None

    # Instructions
    instruction_text_box.setText("""\
             Great job!

Some trials have no equation.
      Just memorize the number.""")
    draw(win=window, stim=instruction_text_box, keyList=['space'])

    # Last example- a baseline trial
    eq_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/20_n.png'))
    comparison_image.setImage(op.join(
        script_dir,
        'stimuli/numerals/25_w.png'))
    eq_image.setSize(set_word_size(eq_image))
    comparison_image.setSize(set_word_size(comparison_image))
    draw(win=window, stim=eq_image, keyList=['space'])
    draw(win=window, stim=comparison_image, keyList=['1'])
    draw(win=window, stim=feedback_image, keyList=['space'])

    # Instructions
    instruction_text_box.setText("""\
          Great job!

     I think you're ready.
Just one last thing to remember.""")
    draw(win=window, stim=instruction_text_box, keyList=['space'])

    # Let's talk about feedback
    instruction_text_box.setText("""\
The feedback image may tell if you're
 correct or incorrect, or it may not.""")
    draw(win=window, stim=instruction_text_box, keyList=['space'])

    feedback_image.setImage(op.join(script_dir, 'stimuli/feedback/positive.png'))
    width, height = feedback_image.size
    new_height = 0.6
    new_shape = (new_height * (width / height), new_height)
    feedback_image.setSize(new_shape)
    draw(win=window, stim=feedback_image, keyList=['space'])

    feedback_image.setImage(op.join(script_dir, 'stimuli/feedback/negative.png'))
    width, height = feedback_image.size
    new_height = 0.6
    new_shape = (new_height * (width / height), new_height)
    feedback_image.setSize(new_shape)
    draw(win=window, stim=feedback_image, keyList=['space'])

    feedback_image.setImage(op.join(script_dir, 'stimuli/feedback/noninformative.png'))
    width, height = feedback_image.size
    new_height = 0.6
    new_shape = (new_height * (width / height), new_height)
    feedback_image.setSize(new_shape)
    draw(win=window, stim=feedback_image, keyList=['space'])

    instruction_text_box.setText("And now we're done.")
    draw(win=window, stim=instruction_text_box, keyList=['space'])
