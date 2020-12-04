import Digraph

"""
This code has been written with respect to the requrements
analysis done in Scenario.txt file in the root directory.
"""

GLOBAL_SUSPECT_LIST = []


def TAKE_INPUT():
    """

    This function will make us to take input
    and return set of total suspects.

    """

    # Initialising total number of suspects.
    temp = input("Enter Total Number of Suspects: ")
    while not temp:
        temp = input("Total Number of Suspect is Required: ")
    TOTAL_SUSPECT = int(temp)

    # Initialising the set of Suspects.
    SUSPECT_SET = {name for name in input(
        "Enter all suspect's name with space between them: \n(CAREFULL SUSPECT NAME(s) ARE ASSUMED TO BE CASE_SENSITIVE AND UNIQUE)\n").split()}

    while len(SUSPECT_SET) != TOTAL_SUSPECT:
        if(len(SUSPECT_SET) < TOTAL_SUSPECT):
            print("Not Sufficient different names provided.Try Again!")
            SUSPECT_SET = {name for name in input().split()}
        else:
            print("Extra different names provided.Try Again!")
            SUSPECT_SET = {name for name in input().split()}

    return SUSPECT_SET


def CHECK_SUBSET(subset, superset):
    """

    This function will check  whether 'subset' is empty set or not
    and whether it is subset of 'superset' or not.

    """
    if len(subset) == 0:
        return False
    return subset.issubset(superset)


def TAKE_STATEMENT(suspect_name, Original_SUSPECT_SET):
    """

    This function will take statement of every suspect in the 
    current situation.

    """
    s_stmnt = input("%s statment type: " % (suspect_name))

    while s_stmnt not in ["a", "b", "c"]:
        s_stmnt = input(
            "%s statment type should be either of a, b or c: " % (suspect_name))

    Original_SUSPECT_SET.discard(suspect_name)

    if s_stmnt == 'a':
        pass

    elif s_stmnt == 'b':
        keep_set = set([])
        keep_set = {st for st in input(
            "Enter %s's target suspects:" % (suspect_name)).split()}

        while not CHECK_SUBSET(keep_set, Original_SUSPECT_SET):
            keep_set = {st for st in input(
                "Entered unknown Names,Try Again for %s's target suspects: " % (suspect_name)).split()}

        Original_SUSPECT_SET = keep_set

    elif s_stmnt == 'c':
        removing_set = set([])
        removing_set = {st for st in input(
            "Enter %s's non-target suspects:" % (suspect_name)).split()}

        while not CHECK_SUBSET(removing_set, Original_SUSPECT_SET):
            removing_set = {st for st in input(
                "Entered unknown Names,Try Again for %s's non-target suspects: " % (suspect_name)).split()}

        for sspt in removing_set:
            Original_SUSPECT_SET.discard(sspt)

    else:
        print("Runtime Problem!!")

    return Original_SUSPECT_SET


def SUSPECT_STATEMENT():
    """

    This function collects all the above function and
    fixed them in a way to reduce the given set of suspect 
    according to given statements of respective suspects.

    """

    SUSPECT_SET = TAKE_INPUT()
    data_graph = {}
    for suspect in SUSPECT_SET:
        target_set = TAKE_STATEMENT(suspect, SUSPECT_SET.copy())
        data_graph[suspect] = target_set


    edge_list = []
    for key in data_graph:
        for item in data_graph[key]:
            edge_list.append((key,item))

    Digraph.drawGraph(list(SUSPECT_SET),edge_list)

    incoming_edge_count = Digraph.get_all_indegree()
    for item in incoming_edge_count:
        print("If %s is Culprit, then %d are saying truth." %
              (item[0], item[1]))


SUSPECT_STATEMENT()