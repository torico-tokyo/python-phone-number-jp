#!/usr/bin/env python3

import unittest

try:
    from .phone_number_jp import split_phone_number
except ImportError:
    from phone_number_jp import split_phone_number

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


if __name__ == '__main__':
    unittest.main()
