def example(a: int, b: str, /, c: float, *, d: int | None = None, e: str = "default") -> bool:
    """
    Example numpydoc doc comment. The summary should be printed on the first new line (not directly after the starting
    triple quotes).

    More details should be added after an empty line in a new section.

    After the function description, list the parameters, their types and a (short) description of what they do in a
    "Parameters" section. Do not include `self` or `cls` if the method is part of a class.
    Separate positional-only from positional-or-keyword from keyword-only arguments with an empty line.
    If a parameter can be omitted (e.g. because it defaults to `None` or another default value), add ", optional" after
    the type. Similarly, if the default value is not `None`, add ", default <default value>" as well.
    If a parameter is a keyword-only argument (i.e., comes after `*` or `*args`), add "kw-only" for more clarity.

    After the parameters, list the return value(s) and what they represent in a "Returns" section.

    If the function is a generator (i.e. `yields` values), add a "Yields" section similar to the "Returns" section after
    the "Returns" section, explaining the yielded values.

    If the function raises exceptions, add a "Raises" section after the "Returns" (or "Yields") section, listing the
    exceptions that can occur and under which conditions they are raised.

    For formatting, use markdown-like syntax, e.g. for *italics*, **bold text**, or `code` (e.g., when referring to
    parameters).

    After the doc comment, leave an empty line before the function definition.

    Parameters
    ----------
    a : int
        Description of a
    b : str
        Description of b.
        More details should be added on a new line.

    c : float
        Description of c

    d : int, optional, kw-only
        Description of d
    e : str, optional, default "default", kw-only
        Description of e

    Returns
    -------
    bool
        Description of the return value

    Raises
    ------
    ValueError
        If an `int` parameter is negative
    """

    return False
