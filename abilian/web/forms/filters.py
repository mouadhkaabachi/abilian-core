# coding=utf-8
"""
Field filters for WTForm.
"""
# Py3k
from __future__ import absolute_import
from past.builtins import basestring


def strip(data):
  """
  Strip data if data is a string
  """
  if data is None:
    return ""
  if not isinstance(data, basestring):
    return data
  return data.strip()


def uppercase(data):
  if not isinstance(data, basestring):
    return data
  return data.upper()


def lowercase(data):
  if not isinstance(data, basestring):
    return data
  return data.lower()
