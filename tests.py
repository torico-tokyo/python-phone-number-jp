#!/usr/bin/env python3

import unittest

try:
    from .phone_number_jp import split_phone_number, PhoneNumberIsNotDigits, \
        PrefixNoMatch, InvaliDigits, insert_hyphens, insert_spaces
except ImportError:
    from phone_number_jp import split_phone_number, PhoneNumberIsNotDigits, \
        PrefixNoMatch, InvaliDigits, insert_hyphens, insert_spaces

test_numbers = [
    ('08011112222', [3, 4, 4]),
    ('09011112222', [3, 4, 4]),
    ('05011112222', [3, 4, 4]),
    ('0311112222', [2, 4, 4]),
    ('0611112222', [2, 4, 4]),
    ('0250111222', [4, 3, 3]),
    ('0251112222', [3, 3, 4]),
    ('0158611222', [5, 2, 3]),
    ('0158111222', [4, 3, 3]),
    ('0746811222', [5, 2, 3]),
]


class PhoneNumberJPTest(unittest.TestCase):

    def test_split(self):
        for phone_number, digits in test_numbers:
            s = split_phone_number(phone_number)
            start = 0
            for segment, digit in zip(s, digits):
                # 桁数があっているかテスト
                self.assertEqual(len(segment), digit)

                # 分割後の数値が正しいかテスト
                segment2 = phone_number[start:start + digit]
                self.assertEqual(segment, segment2)
                start += digit

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
