"""Tests for src/text_utils.py"""
import sys
import os

# خلي سطر sys.path الموجود عندك كما هو

import text_utils


def test_clean_name_whitespace():
    assert text_utils.clean_name("  nora   ali  ") == "Nora Ali"


def test_clean_name_capitalisation():
    assert text_utils.clean_name("NORA ALI") == "Nora Ali"
    assert text_utils.clean_name("nora ali") == "Nora Ali"
