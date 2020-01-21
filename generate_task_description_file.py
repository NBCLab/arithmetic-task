import json

descriptions = {
    'onset': {
        'LongName': 'equation onset',
        'Description': 'Onset of the equation presentation',
        'Units': '[s] second'
    },
    'duration': {
        'LongName': 'equation duration',
        'Description': 'Duration of the equation presentation',
        'Units': '[s] second'
    },
    'comparison_onset': {
        'LongName': 'comparison onset',
        'Description': 'Onset of the comparison value presentation',
        'Units': '[s] second'
    },
    'comparison_duration': {
        'LongName': 'comparison duration',
        'Description': 'Duration of the comparison value presentation',
        'Units': '[s] second'
    },
    'feedback_onset': {
        'LongName': 'feedback onset',
        'Description': 'Onset of the feedback presentation',
        'Units': '[s] second'
    },
    'feedback_duration': {
        'LongName': 'feedback duration',
        'Description': 'Duration of the feedback presentation',
        'Units': '[s] second'
    },
    'first_term': {
        'LongName': 'first term',
        'Description': ('The first term in the equation. '
                        'For baseline trials, this is the only term.'),
    },
    'second_term': {
        'LongName': 'second term',
        'Description': ('The second term in the equation. '
                        'For baseline trials, this is empty.'),
    },
    'operation': {
        'LongName': 'operation',
        'Description': 'Equation operation. For baseline trials, this is empty.',
        'Levels': {
            'add': ('The first term is added to the second term.'),
            'subtract': ('The second term is subtracted from the first term.'),
            'divide': ('The first term is divided by the second term'),
            'multiply': ('The first term is multiplied by the second term'),
        }
    },
    'comparison': {
        'LongName': 'comparison value',
        'Description': 'Number against which to compare equation solution',
    },
    'solution': {
        'LongName': 'solution value',
        'Description': 'Solution to the equation. For baseline trials this '
                       'is the same as "equation".',
    },
    'rounded_difference': {
        'LongName': 'rounded difference',
        'Description': ('Difference between the solution and the comparison '
                        'value, rounded to the nearest integer.'),
    },
    'feedback_type': {
        'LongName': 'feedback type',
        'Description': 'Whether trial feedback will be informative or not.',
        'Levels': {
            'informative': ('Feedback will indicate whether or not response was correct.'),
            'uninformative': ('Feedback will not indicate whether or not response was correct.'),
        }
    },
    'accuracy': {
        'LongName': 'accuracy',
        'Description': 'Accuracy of trial',
        'Levels': {
            'incorrect': 'Incorrect response',
            'correct': 'Correct response',
            'no_response': 'No response'
        }
    },
    'stim_file_first_term': {
        'LongName': 'First-term stimulus file',
        'Description': ('File for the first term in the equation. '
                        'For baseline trials, this is the only value.')
    },
    'stim_file_operator': {
        'LongName': 'Operator stimulus file',
        'Description': ('File for the operator in the equation. '
                        'This value is empty for baseline trials.')
    },
    'stim_file_second_term': {
        'LongName': 'Second-term stimulus file',
        'Description': ('File for the second term in the equation. '
                        'This value is empty for baseline trials.')
    },
    'stim_file_comparison': {
        'LongName': 'Comparison stimulus file',
        'Description': 'File for the comparison value.'
    },
    'stim_file_feedback': {
        'LongName': 'Feedback stimulus file',
        'Description': 'File for the trial feedback.'
    },
    'equation_representation': {
        'LongName': 'Equation representation',
        'Description': ('Whether the equation is presented in "word" or '
                        '"numeric" form.'),
        'Levels': {
            'word': 'Stimuli presented in word form',
            'numeric': 'Stimuli presented as numerals',
        }
    },
    'comparison_representation': {
        'LongName': 'Comparison value representation',
        'Description': ('Whether the comparison value is presented in "word" '
                        'or "numeric" form.'),
        'Levels': {
            'word': 'Stimuli presented in word form',
            'numeric': 'Stimuli presented as numerals',
        }
    },
}

with open('task-math_events.json', 'w') as fo:
    json.dump(descriptions, fo, sort_keys=True, indent=4)
