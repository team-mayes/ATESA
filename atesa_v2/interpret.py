"""
This portion of the program is responsible for handling update of the results, checking global termination criteria, and
implementing the calls to JobType methods to control the value of the thread.coordinates attribute for the next step.
"""

from atesa_v2 import factory

def interpret(thread, allthreads, running, settings):
    """
    The main function of interpret.py. Makes calls to JobType methods to update results, check termination criteria, and
    update thread.coordinates

    Parameters
    ----------
    thread : Thread
        The Thread object on which to act
    allthreads : list
        The list of all extant Thread objects
    running : list
        The list of all currently running Thread objects
    settings : argparse.Namespace
        Settings namespace object

    Returns
    -------
    termination: bool
        True if a global termination criterion has been met; False otherwise

    """

    jobtype = factory.jobtype_factory(settings.job_type)
    termination = False

    if jobtype.check_for_successful_step(thread):                               # ensure this step did not crash/fail
        termination = jobtype.check_termination(thread, allthreads, settings)   # check global termination criteria
        jobtype.update_results(thread, allthreads, settings)                    # update results as needed
    running = jobtype.algorithm(thread, allthreads, settings)                   # set thread parameters for next step

    return termination, running
