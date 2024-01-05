#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a sentence and its first character. If empty, returns (0, None)."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
