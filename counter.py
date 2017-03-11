""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import pickle


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """

    if exists(file_name) and not reset:
            # this the case that the file already exists and you have to increment the contents.
            counter = 0
            fi1 = open(file_name, 'rb+')
            fi1.seek(0, 0)
            contents = pickle.load(fi1)
            fi1.seek(0, 0)
            counter = contents + 1  # incrementing contents
            pickle.dump(counter, fi1)  # putting contents back in
            fi1.close()
            return counter
    else:
        """in all other cases (file doesnt already exist or file does exist and
        you need to reset) this just overrights anything and sets the contents to 1
        """
        fi1 = open(file_name, 'wb')
        pickle.dump(1, fi1) # adding a 1
        fi1.close()
        return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
