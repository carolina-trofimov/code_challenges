"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

        #create a counter
    counter = 0
    # loop over string 
    for char in phrase:
        # if char is ")"
        if char == ")":
            #counter decrements by 1
            counter -= 1
            #if counter is -1
            if counter == -1:
                #return False
                return False
        
        #if char is "(":
        if char == "(":
            #increment counter by 1
            counter += 1
    #if counter is 0:
    if counter == 0:
        # return True
        return True
    #else:
    else:
        #return False
        return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
