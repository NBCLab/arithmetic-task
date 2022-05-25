# arithmetic-task
A basic arithmetic task implemented with PsychoPy.

This repository has two PsychoPy tasks: `training.py` and `arithmetic_task.py`.

The script `training.py` is used for out-of-scanner training to ensure that participants understand the task.

The script `arithmetic_task.py` is the in-scanner task.
This task has two runs of 7.5 minutes.

## Configuration files

## Implementation details

Each run of the task lasts 450 seconds.
The task begins with six seconds of fixation.
Each trial consists of six stages:

1.  The formula.
    The formulas consist of two numbers, each ranging from 1 to 30, and an operator (i.e., +, -, *, /).
    Participants then try to mentally solve the formula.
    The formula is presented for 1 to 3 seconds, with the exact duration selected from a uniform distribution from 1 - 3,
    and then rounded to the nearest tenth of a second.
2.  Inter-stimulus interval (ISI).
    The first ISI is a red dot at the center of the screen.
    This ISI lasts for 2 to 8 seconds, with exact duration selected from a right-skewed Gumbel distribution with mean of 4 seconds,
    after which the value is restricted to 2-8 seconds, and then rounded to nearest 0.1 seconds.
3.  Comparison value.
    A comparison value is then presented.
    The value will be an integer that is within 10 of the actual solution to the formula.
    Participants must respond if the actual solution is smaller than (button 1), equal to (button 2),
    or greater than (button 3) the comparison value.
    The difference between the comparison value and the actual solution is expected to influence trial difficulty,
    with more different comparison and actual values being easier than closer ones.
4.  Inter-stimulus interval (ISI).
    The second ISI is a white dot at the center of the screen.
    This ISI's duration is selected based on the same procedure as the first ISI.
5.  Feedback.
    Next is a feedback screen.
    The feedback may be informative or noninformative.
    The noninformative feedback is a neutral emoji.
    The informative feedback is either a smiling emoji, if the participant was correct, or a frowning emoji,
    if the participant was incorrect.
6.  Inter-trial interval (ITI).
    The ITI duration is selected based on the same procedure as the ISIs.

Both the formula and the comparison value may be presented either in numerical form or word form.
This manipulation was included based on the triple code model \cite{skagenholt2018examining}.
We initially planned to include analog nonsymbolic magnitude representations,
but we found that this was too difficult for participants.

After 24 trials, a final white fixation dot will appear until the task ends.
8 / 24 trials are "baseline" trials,
in which the "formula" stage will just be a single value that the participant must compare to the comparison value.

The task is implemented in PsychoPy \cite{peirce2007psychopy,peirce2009generating}.

## References

```BibTeX
@article{peirce2007psychopy,
  title={PsychoPy—psychophysics software in Python},
  author={Peirce, Jonathan W},
  journal={Journal of neuroscience methods},
  volume={162},
  number={1-2},
  pages={8--13},
  year={2007},
  publisher={Elsevier}
}

@article{peirce2009generating,
  title={Generating stimuli for neuroscience using PsychoPy},
  author={Peirce, Jonathan W},
  journal={Frontiers in neuroinformatics},
  volume={2},
  pages={10},
  year={2009},
  publisher={Frontiers}
}

@article{skagenholt2018examining,
  title={Examining the Triple Code Model in numerical cognition: An fMRI study},
  author={Skagenholt, Mikael and Tr{\"a}ff, Ulf and V{\"a}stfj{\"a}ll, Daniel and Skagerlund, Kenny},
  journal={PLoS One},
  volume={13},
  number={6},
  pages={e0199247},
  year={2018},
  publisher={Public Library of Science San Francisco, CA USA}
}
```
