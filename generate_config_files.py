# coding: utf-8
import json
import numpy as np
from collections import Counter
from scipy.stats import gumbel_r
import pandas as pd

FEEDBACK_DURATION = 0.5
EQ_DUR_RANGE = (1, 3)
COMP_DUR_RANGE = (1, 3)
INTERVAL_RANGE = (2, 8)  # max determined to minimize difference from TASK_TIME

N_RUNS = 2
N_TRIALS = 24  # total
# General
TOTAL_DURATION = 450.
TASK_TIME = 438  # time for trials in task
LEAD_IN_DURATION = 6  # fixation before trials


def get_hist(vals, value_range):
    counter = Counter(vals)
    for v in value_range:
        if v not in counter.keys():
            counter[v] = 0
    x = sorted(counter.keys())
    y = [counter[x_val] for x_val in x]
    return x, y


def determine_timing(n_trials=24, null_rate=0.33,
                     operators=['*', '+', '-', '/'],
                     num_types=['numeric', 'word'],
                     feedback_types=['informative', 'noninformative'],
                     seed=None):
    """
    Generate configuration files.

    Parameters
    ----------
    n_runs : int
        Number of runs
    n_trials : int
        Number of trials
    null_rate : float
        Proportion of trials to set as null trial type.
        Default set to 1/3 per Dr. Aaron Mattfeld's recommendation.
    operators : list
        List of valid operations to include
    num_types : list
        Number representations to include. May include numeric, word, and/or analog.
    feedback_types : list
        Feedback types to include. May include informative and uninformative.
    """
    n_null_trials = int(np.ceil(n_trials * null_rate))
    n_math_trials = n_trials - n_null_trials

    # Timing
    mu = 4  # mean of 4s
    raw_intervals = gumbel_r.rvs(size=100000, loc=mu, scale=1)
    possible_intervals = np.round(raw_intervals, 1)
    # crop to 2-8s
    possible_intervals = possible_intervals[possible_intervals >= INTERVAL_RANGE[0]]
    possible_intervals = possible_intervals[possible_intervals <= INTERVAL_RANGE[1]]

    missing_time = np.finfo(dtype='float64').max
    if not seed:
        seed = np.random.randint(1000, 9999)

    while (not np.isclose(missing_time, 0.0, atol=10)) or (missing_time < 0):
        state = np.random.RandomState(seed=seed)
        eq_durations = state.uniform(EQ_DUR_RANGE[0], EQ_DUR_RANGE[1], n_trials)
        eq_durations = np.round(eq_durations, 1)
        comp_durations = state.uniform(COMP_DUR_RANGE[0], COMP_DUR_RANGE[1], n_trials)
        comp_durations = np.round(comp_durations, 1)
        fdbk_durations = np.ones(n_trials) * FEEDBACK_DURATION
        isi1s = state.choice(possible_intervals, size=n_trials, replace=True)
        isi2s = state.choice(possible_intervals, size=n_trials, replace=True)
        itis = state.choice(possible_intervals, size=n_trials, replace=True)

        missing_time = TASK_TIME - np.sum([eq_durations.sum(), comp_durations.sum(),
                                           fdbk_durations.sum(),
                                           isi1s.sum(), isi2s.sum(), itis.sum()])
        seed += 1

    full_operators = operators * int(np.ceil(n_math_trials / len(operators)))
    full_num_types = num_types * int(np.ceil(n_trials / len(num_types)))
    full_feedback_types = feedback_types * int(np.ceil(n_trials / len(feedback_types)))

    # Get distribution of difference scores to control math difficulty
    # We want a sort of flattened normal distribution for this
    value_range = 20
    raw_difference_scores = np.random.binomial(n=value_range, p=0.5, size=100000) - int(value_range / 2)
    x = np.arange(value_range+1, dtype=int) - int(value_range / 2)
    x, y = get_hist(raw_difference_scores, x)
    uniform = np.ones(len(x)) * np.mean(y)
    updated_distribution = np.mean(np.vstack((y, uniform)), axis=0)
    probabilities = updated_distribution / np.sum(updated_distribution)

    # Slightly more complicated approach chosen over np.random.choice
    # to make numbers of trials with each type as balanced as possible
    chosen_operators = np.random.choice(full_operators, n_math_trials, replace=False)
    chosen_equation_num_types = np.random.choice(full_num_types, n_trials, replace=False)
    chosen_comparison_num_types = np.random.choice(full_num_types, n_trials, replace=False)
    chosen_feedback_types = np.random.choice(full_feedback_types, n_trials, replace=False)

    difference_scores = np.random.choice(x, size=n_trials, p=probabilities)
    difference_scores = [int(ds) for ds in difference_scores]

    equations, comparisons, solutions = [], [], []

    # Set order of trial types. 1 = math, 0 = baseline
    ttype_dict = {0: 'baseline', 1: 'math'}
    trial_types = np.ones(n_trials, int)
    trial_types[:n_null_trials] = 0
    np.random.shuffle(trial_types)
    math_counter = 0

    for j_trial in range(n_trials):
        if trial_types[j_trial] == 1:
            first_val = str(np.random.randint(1, 31))
            second_val = str(np.random.randint(1, 31))
            operator = chosen_operators[math_counter]
            # If the result of division would be less than 1, flip the values
            if operator == '/' and int(first_val) < int(second_val):
                first_val, second_val = second_val, first_val
            equation = first_val + operator + second_val
            solution = eval(equation)
            math_counter += 1
        else:
            solution = np.random.randint(1, 31)
            equation = str(solution)

        comparison = int(np.round(solution + difference_scores[j_trial]))
        equations.append(equation)
        comparisons.append(comparison)
        solutions.append(solution)

    timing_dict = {
        'trial_type': [ttype_dict[tt] for tt in trial_types],
        'equation': equations,
        'solution': solutions,
        'comparison': comparisons,
        'equation_representation': chosen_equation_num_types,
        'comparison_representation': chosen_comparison_num_types,
        'feedback': chosen_feedback_types,
        'rounded_difference': difference_scores,
        'equation_duration': eq_durations,
        'isi1': isi1s,
        'comparison_duration': comp_durations,
        'isi2': isi2s,
        'feedback_duration': fdbk_durations,
        'iti': itis,
    }
    df = pd.DataFrame(timing_dict)
    return df, seed


def main():
    n_files = 200
    seed = 1
    for i_file in range(1, n_files+1):
        df, seed = determine_timing(n_trials=N_TRIALS, seed=seed)
        df.to_csv('config/config_{0:05d}.tsv'.format(i_file),
                  sep='\t', index=False, float_format='%.1f')


if __name__ == '__main__':
    main()
