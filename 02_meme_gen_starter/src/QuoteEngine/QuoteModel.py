"""Create a Model class to hold quotes."""


class QuoteModel():
    """Create a QuoteModel class to hold quotes."""

    def __init__(self, body, author):
        """Store parameter values in local variable.

        Arguments:
            body {str} -- an inspiring quote.
            author {str} -- author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return stored parameter values in local variable.

        Returns:
             {str} -- quote and its author.
        """
        return f'<{self.body}, {self.author}>'
