#!/usr/bin/python3
"""function class MyInt that inherits from int."""


class MyInt(int):
    """int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator == behavior."""
        return self.real == value
