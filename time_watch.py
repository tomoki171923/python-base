# -*- coding: utf-8 -*-
'''
This class has some functions to measure the action time.
'''
import time


class TimeWatch:

    ''' constructor.
    Args:
        log_file (bool, optional): write message on the log file or not.
    '''

    def __init__(self, log_file: bool = False):
        self.__actions = dict()
        if log_file is True:
            self.__file = open(file=f'./time_watch.log', mode='w')
        else:
            self.__file = None

    ''' destructor.
    Args:
        log_file (bool, optional): write message on the log file or not.
    '''

    def __del__(self):
        if self.__file is not None:
            self.__file.close()
            del self.__file
        del self.__actions

    ''' start measuring time.
    Args:
        action_name (str): an action name.
    '''

    def start(self, action_name: str) -> None:
        start_time = time.time()
        self.__actions[action_name] = {
            'start': start_time
        }

    ''' stop measuring time.
    Args:
        action_name (str): an action name.
    '''

    def stop(self, action_name: str) -> None:
        start_time = self.__actions[action_name]["start"]
        end_time = time.time()
        elapsed_time = end_time - start_time
        item = {
            'end': end_time,
            'elapsed_time': elapsed_time
        }
        self.__actions[action_name].update(item)

    ''' print the elapsed time of action.
    Args:
        action_name (str): an action name.
    '''

    def print(self, action_name: str) -> None:
        elapsed_time = self.__actions[action_name]["elapsed_time"]
        message: str = f"[action name : {action_name} ] elapsed time : {elapsed_time * 1000}[ms]"
        print(message)
        if self.__file is not None:
            # if log_file opsion is True, write message on the log file
            self.__file.write(message + '\n')

    ''' clear instance variable.
    '''

    def clear(self) -> None:
        self.__actions.clear()
