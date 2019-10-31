# coding: utf-8
import json
import itertools as it
import numpy as np


def math_gen(n_runs, n_trials,
             operators=['*', '+', '-', '/'],
             num_types=['numeric', 'analog'],
             feedback_types=['informative', 'noninformative']):

    full_operators = operators * int(np.ceil(n_trials / len(operators)))
    full_num_types = num_types * int(np.ceil(n_trials / len(num_types)))
    full_feedback_types = feedback_types * int(np.ceil(n_trials / len(feedback_types)))

    run_dict = {}
    for i_run in range(1, n_runs + 1):
        run_dict[i_run] = []
        difference_scores = np.random.binomial(n=20, p=0.5, size=n_trials) - 10
        difference_scores = [int(ds) for ds in difference_scores]

        # Slightly more complicated approach chosen over np.random.choice
        # to make numbers of trials with each type as balanced as possible
        chosen_operators = np.random.choice(full_operators, n_trials, replace=False)
        chosen_num_types = np.random.choice(full_num_types, n_trials, replace=False)
        chosen_feedback_types = np.random.choice(full_feedback_types, n_trials, replace=False)

        equations, comparisons = [], []
        for j_trial in range(n_trials):
            first_val = str(np.random.randint(1, 31))
            second_val = str(np.random.randint(1, 31))
            operator = chosen_operators[j_trial]
            equation = first_val + operator + second_val
            result = eval(equation)
            comparison = int(np.round(result + difference_scores[j_trial]))
            equations.append(equation)
            comparisons.append(comparison)
            run_dict[i_run].append({
                'equation': equation,
                'solution': result,
                'comparison': comparison,
                'representation': chosen_num_types[j_trial],
                'feedback': chosen_feedback_types[j_trial],
                'rounded_difference': difference_scores[j_trial]
            })

    return run_dict


if __name__ == '__main__':
    subject_dict = {}
    n_runs = 2
    n_trials = 5
    for subj_no in range(1, 21):
        subject_id = '{0:02d}'.format(subj_no)
        subject_dict[subject_id] = {}
        for sess_no in range(1, 21):
            session_id = '{0:02d}'.format(sess_no)
            subject_dict[subject_id][session_id] = math_gen(n_runs=n_runs, n_trials=n_trials)

    with open('config/subject_config.json', 'w') as fw:
        json.dump(subject_dict, fw, sort_keys=True, indent=4)
