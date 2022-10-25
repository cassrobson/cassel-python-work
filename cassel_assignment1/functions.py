"""
-------------------------------------------------------
functions file
-------------------------------------------------------
Author:  Cassel Robson
ID:      210507000
Email:   robs7000@mylaurier.ca
__updated__ = "2022-01-13"
-------------------------------------------------------
"""
# Imports
import numpy as np
# Constants


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    check = []
    for i in values:
        if i in check:
            values.remove(i)
        else:
            check.append(i)

    return


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    vowels = 'aeiouAEIOU'
    list_s = list(s)
    for i in list_s:
        if i in vowels:
            list_s.remove(i)
    out = ''.join(list_s)
    return out


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    line = fv.readline().strip()
    while line != '':
        for i in line:
            if i.isupper() == True:
                u += 1
            elif i.islower() == True:
                l += 1
            elif i.isdigit() == True:
                d += 1
            elif i == ' ':
                w += 1
            else:
                r += 1
        line = fv.readline().strip()
    return u, l, d, w, r


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """

    if (year % 400 == 0) and (year % 100 != 0):
        leap_year = True
    elif (year % 4 == 0) and (year % 100 != 0):
        leap_year = True

    else:
        leap_year = False

    return leap_year

    return leap_year


def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    reverse = ''
    for i in range(1, len(s) + 1):
        reverse += s[-i]

    lowered = reverse.lower()
    if lowered == s.lower():
        palindrome = True
    else:
        palindrome = False

    return palindrome


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    md = 0
    for i in range(len(a) - 1):
        rd = abs((a[i + 1]) - (a[i]))
        if rd > md:
            md = rd
    return md


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    a_transpose = np.transpose(a)

    return a_transpose


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """

    count = 0
    large = 0
    small = 10000000
    total = 0

    for i in a:
        for j in i:
            if j > large:
                large = j
            if j < small:
                small = j
            total += j
            count += 1

    average = total / count

    return large, small, total, average


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    i = 0
    count = 0
    pl = ''
    vowels = 'aeiouAEIOU'
    if word[0] in vowels:
        pl = word + 'way'
    else:
        while word[i] not in vowels:
            count += 1
            i += 1
        pl = word[count:] + word[:count] + 'ay'

    if word[0].isupper() == True:
        pl = pl.capitalize()

    return pl
