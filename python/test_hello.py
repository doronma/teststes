"""
Simple Test File
"""


from hello import hello


class TestHello:
    """
    Test Class for hello.py
    """

    def test_hello_returns_hello_world(self):
        """
        Test the hello function with the input "World".
        This is a valid edge case since the function accepts any string input.
        """
        result = hello("World")
        assert result == "Hello World", "Expected 'Hello World' for input 'World'"

    def test_hello_empty_input(self):
        """
        Test the hello function with an empty string input.
        This is a valid edge case since the function accepts any string input.
        """
        result = hello("")
        assert result == "Hello ", "Expected 'Hello ' for empty input"

    def test_hello_returns_greeting_with_name(self):
        """
        Test that the hello function returns a greeting with the given name.

        This test verifies that the hello function correctly formats and
        returns a greeting string that includes the provided name.
        """
        result = hello("World")
        assert result == "Hello World"
