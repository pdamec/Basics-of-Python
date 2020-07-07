"""Module4/task1: MadLib class consisting of text replacement utils."""
import os

import pyinputplus as pyip


PLACEHOLDERS = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


class MadLib:
    """Class used for replacing strings in files."""

    def __init__(self, filename):
        """:param filename: path to the input file."""
        self.input = self.load_input_text(filename)

        self.replacements = {}
        self.output = ''

    @staticmethod
    def load_input_text(filename) -> str:
        """Load text from input file.

        :param filename: path to the input file.
        :return text from file.
        """
        return open(filename, 'r').read()

    def replace_placeholders(self):
        """Replace placeholders and set output instance variable."""
        output = self.input
        for check, replacer in list(self.replacements.items()):
            output = output.replace(check, replacer)
        self.output = output

    def input_replacements(self):
        """Ask user for replacements and create config data."""
        replacements = {}
        for placeholder in PLACEHOLDERS:
            replacement = pyip.inputStr(f'Enter a {placeholder.lower()}:')
            replacements.update({placeholder: replacement})
        self.replacements = replacements

    def display_text(self):
        """Display replaced text."""
        print(self.output)

    def save_output_text(self, filename):
        """Save replaced text to a given file."""
        with open(filename, 'w') as fout:
            fout.write(self.output)


if __name__ == '__main__':
    # Paths
    text_dir = os.path.join(os.getcwd(), 'resources')
    input_file = os.path.join(text_dir, 'example.txt')
    output_file = os.path.join(text_dir, 'output.txt')

    # MadLib object
    mad_lib = MadLib(input_file)
    mad_lib.input_replacements()  # get replacements from user.
    mad_lib.replace_placeholders()
    mad_lib.display_text()
    mad_lib.save_output_text(output_file)  # Save replaced bytes to output file.
