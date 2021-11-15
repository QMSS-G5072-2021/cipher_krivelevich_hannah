#!/usr/bin/env python

"""Tests for `cipher_hek2125` package."""


import pytest

from cipher_hek2125 import cipher_hek2125
from cipher_hek2125 import cli


class TestCipher_hek2125(unittest.TestCase):
    """Tests for `cipher_hek2125` package."""
    
  def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

    def test_Single_Word_Cipher():
        example = 'sketch'
        Single_Word_Shift = 3
        expected = 'vnhwfk'
        actual = cipher(example, Single_Word_Shift)
        assert actual == expected
