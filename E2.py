import numpy as np

def compare_goals(goals_to_compare: int, matches: list):
    """
    Function to compare if goals in compared match are less or equal than the base match.
    
    INPUT
    --------------------------------------------------
    goals_to_compare: int
    Number of goals to be compared to.

    matches: list
    Matches in which the comparison is made.

    OUTPUT
    --------------------------------------------------
    A list (list data type) of 1 when matches fullfil the condition and 0 when do not.
    """
    return [1 if m <= goals_to_compare else 0 for m in matches]


def matches_comparison_counts(base_team: list, compared_team: list):
    """
    Function to get a list of counts where matches fulfill the requirements of the exercise.

    INPUT
    --------------------------------------------------
    base_team: list
    Team to be compared to.

    compared_team: list
    Team in which the comparison is made.

    OUTPUT
    --------------------------------------------------
    A list (list data type) of count of matches in which the condition is met.
    """
    assert len(base_team) <= 105, '"base_team" debe tener 105 elementos como máximo'
    assert 2 <= len(compared_team), '"compared_team" debe tener 2 elementos como mínimo'

    assert 1 <= min(base_team) and max(base_team) <= 109, 'elementos en lista deben ser mayores o iguales a 1 y menores o iguales a 109'
    assert 1 <= min(compared_team) and max(compared_team) <= 109, 'elementos en lista deben ser mayores o iguales a 1 y menores o iguales a 109'

    res = []

    for goals_in_match in base_team:
        matches = compare_goals(goals_to_compare=goals_in_match, matches=compared_team)

        res.append(sum(matches))

    return res


def generate_matches_list(min_goals: int, max_goals: int, total_matches: int):
    """
    Function to generate a random list.

    INPUT
    --------------------------------------------------
    min_goals: int
    Minimum number of goals on matches (low range).

    max_goals: int
    Maximum number of goals on matches (high range).
    
    total_matches: int
    Total number of matches (sum of elements in list) to generate.

    OUTPUT
    --------------------------------------------------
    A list randomly generated with input data.
    """
    return list(np.random.randint(low=min_goals, high=max_goals, size=total_matches))


def random_tests(min_goals: int, max_goals: int, total_matches1: int, total_matches2: int):
    """
    Function to get a list of counts where matches fulfill the requirements of the exercise based on two randomly generated lists.

    INPUT
    --------------------------------------------------
    min_goals: int
    Minimum number of goals on matches (low range).
    
    max_goals: int
    Maximum number of goals on matches (high range).
    
    total_matches1: int
    Total number of matches (lenght of list) to generate for team1.

    total_matches2: int
    Total number of matches (lenght of list) to generate for team2.
    """
    team1 = generate_matches_list(min_goals=min_goals, max_goals=max_goals, total_matches=total_matches1)
    team2 = generate_matches_list(min_goals=min_goals, max_goals=max_goals, total_matches=total_matches2)

    print('Se han generado las siguientes listas:')
    print('equipoA:', team1)
    print('equipoB:', team2)

    print('Resultado para cada partido del equipoA:')
    print(matches_comparison_counts(base_team=team1, compared_team=team2))
    
    print('Resultado para cada partido del equipoB:')
    print(matches_comparison_counts(base_team=team2, compared_team=team1))


def counts(
    given_teams: bool = True, base_team: list = [2, 4], compared_team: list =  [1, 2, 3],
    min_goals: int = 1, max_goals: int = 109, total_matches1: int = 2, total_matches2: int = 2
):
    """
    Function counts that lets you choose whether to give the two teams' lists as input or to generate random samples.
    In the latter case, the function will display the result of comparing teamA VS teamB and visceversa, otherwhise, the function will display
    the result of comparing base_team VS compared_team.

    INPUT
    --------------------------------------------------
    given_teams: bool (default True)
    Parameter to determine if a manual input is given (True) or if the function will generate the sample (False).

    base_team: list (default [2, 4])
    If given_teams=True
    Team to be compared to.

    compared_team: list (default [1, 2, 3])
    If given_teams=True
    Team in which the comparison is made.

    min_goals: int (default 1)
    If given_teams=False
    Minimum number of goals on matches (low range).

    max_goals: int (deafult 109)
    If given_teams=False
    Maximum number of goals on matches (high range).

    total_matches1: int (default 2)
    If given_teams=False
    Total number of matches (lenght of list) to generate for team1.

    total_matches2: int (default 2)
    If given_teams=False
    Total number of matches (lenght of list) to generate for team2.
    """
    if given_teams:
        print('equipoA:', compared_team)
        print('equipoB:', base_team)

        print('Resultado de comparar los partidos del equipoB con los del equipoA')
        print(matches_comparison_counts(base_team=base_team, compared_team=compared_team))
    else:
        random_tests(min_goals=min_goals, max_goals=max_goals, total_matches1=total_matches1, total_matches2=total_matches2)
