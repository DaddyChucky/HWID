# Used as is, see https://github.com/DaddyChucky/UNIVERSAL_SCRAPER for more information about this file.

__title__       = 'taste_the_rainbow.py'
__doc__         = 'Makes text decoration.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo (https://github.com/DaddyChucky/HWID).'


###
#   --> TASTE_THE_RAINBOW <--
###


class TextDecoration:
    """
    Interface for text decoration used to output text
    """
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKCYAN      = '\033[96m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'


def print_header(category: str, text_to_print: str) -> None:
    """
    Prints text as header

    Args:
        category        (str): Message category
        text_to_print   (str): Text to print (output)
            
    Returns:
        None
    """
    print(
        TextDecoration.HEADER + TextDecoration.BOLD + "[" + category + "] > " + TextDecoration.ENDC + TextDecoration.OKBLUE +
        text_to_print + TextDecoration.ENDC)


def print_success(category: str, text_to_print: str) -> None:
    """
    Prints text as success

    Args:
        category        (str): Message category
        text_to_print   (str): Text to print (output)
            
    Returns:
        None
    """
    print(
        TextDecoration.HEADER + TextDecoration.BOLD + "[" + category + "] > " + TextDecoration.ENDC + TextDecoration.OKGREEN +
        text_to_print + " ✓ " + TextDecoration.ENDC)


def print_warning(category: str, text_to_print: str) -> None:
    """
    Prints text as warning

    Args:
        category        (str): Message category
        text_to_print   (str): Text to print (output)
            
    Returns:
        None
    """
    print(
        TextDecoration.HEADER + TextDecoration.BOLD + "[" + category + "] > " + TextDecoration.ENDC + TextDecoration.WARNING +
        text_to_print + " ⚠ " + TextDecoration.ENDC)


def print_failure(category: str, text_to_print: str) -> None:
    """
    Prints text as failure

    Args:
        category        (str): Message category
        text_to_print   (str): Text to print (output)
            
    Returns:
        None
    """
    print(
        TextDecoration.HEADER + TextDecoration.BOLD + "[" + category + "] > " + TextDecoration.ENDC + TextDecoration.FAIL +
        text_to_print + " ✗ " + TextDecoration.ENDC)