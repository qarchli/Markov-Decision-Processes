import csv


def read_data(transition_file, rewards_file):
    transitions = {}
    rewards = {}

    # read transitions from file and store it to a variable
    with open(transition_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] in transitions:
                if row[1] in transitions[row[0]]:
                    transitions[row[0]][row[1]].append((float(row[3]), row[2]))
                else:
                    transitions[row[0]][row[1]] = [(float(row[3]), row[2])]
            else:
                transitions[row[0]] = {row[1]: [(float(row[3]), row[2])]}

    # read rewards file and save it to a variable
    with open(rewards_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rewards[row[0]] = float(row[1]) if row[1] != 'None' else None

    return transitions, rewards


def pretty_print(d, indent=0):
    '''
    pretty print dictionnaries
    '''
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty_print(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))
