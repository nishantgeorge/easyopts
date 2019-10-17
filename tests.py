from unittest import TestCase, main

from easyopts import parseargs, OptionParsingError


class EasyOptionsTestCase(TestCase):
    
    def test_valid_options(self):
        """
        Test cases for valid options which should be successfully parsed.
        """

        # Option names with letters and numbers
        args = ["--option1", "value1", "--option2", "value2"]
        opts = parseargs(args)
        self.assertEqual(opts, {"option1": "value1", "option2": "value2"})

        # Option names with hyphens
        args = ["--option-one", "value1"]
        opts = parseargs(args)
        self.assertEqual(opts, {"option-one": "value1"})

        # Latest value should be used for repeated arguments
        args = ["--option", "value1", "--option", "value2"]
        opts = parseargs(args)
        self.assertEqual(opts, {"option": "value2"})
    
    def test_invalid_options(self):
        """
        Test cases for invalid options which should be rejected with an OptionParsingError.
        """

        # Option name starting with a non-letter character
        args = ["--1option", "value1"]
        with self.assertRaises(OptionParsingError) as ctx:
            opts = parseargs(args)
        self.assertIn("1option", str(ctx.exception))
        
        # Option name starting with a hyphen
        args = ["---option", "value1"]
        with self.assertRaises(OptionParsingError) as ctx:
            opts = parseargs(args)
        self.assertIn('-option', str(ctx.exception))
        
        # Odd number of arguments (unmatched option names and values)
        args = ["--option", "value1", '--option2']
        with self.assertRaises(OptionParsingError) as ctx:
            opts = parseargs(args)
        self.assertIn("odd number of arguments", str(ctx.exception).lower())
            



if __name__ == '__main__':
    main()
