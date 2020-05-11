#!/usr/bin/env python3

import unittest

try:
    from .phone_number_jp import split_phone_number, PhoneNumberIsNotDigits, \
        PrefixNoMatch, InvaliDigits, insert_hyphens, insert_spaces, \
        split_phone_number_no_fail
except ImportError:
    from phone_number_jp import split_phone_number, PhoneNumberIsNotDigits, \
        PrefixNoMatch, InvaliDigits, insert_hyphens, insert_spaces, \
        split_phone_number_no_fail

test_numbers = [
    ('08011112222', ('080', '1111', '2222')),
    ('09011112222', ('090', '1111', '2222')),
    ('05011112222', ('050', '1111', '2222')),
    ('0311112222', ('03', '1111', '2222')),
    ('0611112222', ('06', '1111', '2222')),
    ('0250111222', ('0250', '111', '222')),
    ('0251112222', ('025', '111', '2222')),
    ('0158611222', ('01586', '11', '222')),
    ('0158111222', ('0158', '111', '222')),
    ('0746811222', ('07468', '11', '222')),
]


class PhoneNumberJPTest(unittest.TestCase):

    def test_split(self):
        for before, after in test_numbers:
            self.assertEqual(split_phone_number(before), after)

    def test_no_number(self):
        with self.assertRaises(PhoneNumberIsNotDigits):
            split_phone_number('0901111222a')

    def test_no_match(self):
        with self.assertRaises(PrefixNoMatch):
            split_phone_number('09111112222')
        with self.assertRaises(PrefixNoMatch):
            split_phone_number('10011112222')

    def test_invalid_digits(self):
        with self.assertRaises(InvaliDigits):
            split_phone_number('091112222')

    def test_no_fail(self):
        self.assertEqual(split_phone_number_no_fail(''), ('', '', ''))
        self.assertEqual(split_phone_number_no_fail(' '), ('', '', ''))
        self.assertEqual(split_phone_number_no_fail('\n'), ('', '', ''))
        self.assertEqual(split_phone_number_no_fail('0311112222'),
                         ('03', '1111', '2222'))
        self.assertEqual(split_phone_number_no_fail('08011112222'),
                         ('080', '1111', '2222'))
        self.assertEqual(split_phone_number_no_fail('03HELLO2222'),
                         ('', '', ''))
        self.assertEqual(split_phone_number_no_fail('080=1111=2222'),
                         ('', '', ''))
        self.assertEqual(split_phone_number_no_fail('080ー1111ー2222'),
                         ('', '', ''))
        self.assertEqual(split_phone_number_no_fail('こんにちは'),
                         ('', '', ''))

    def test_insert_hyphens(self):
        self.assertEqual(
            insert_hyphens('0311112222'), '03-1111-2222')
        self.assertEqual(
            insert_hyphens('09011112222'), '090-1111-2222')
        self.assertEqual(
            insert_hyphens('090-1111-2222'), '090-1111-2222')

    def test_insert_spaces(self):
        self.assertEqual(
            insert_spaces('0158611222'), '01586 11 222')
        self.assertEqual(
            insert_spaces('0158111222'), '0158 111 222')
        self.assertEqual(
            insert_spaces('01586 11 222'), '01586 11 222')


if __name__ == '__main__':
    unittest.main()
