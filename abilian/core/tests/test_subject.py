# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from builtins import str


from abilian.core.models.subjects import User

def test_non_ascii_password():
  """Ensure we can store and test non-ascii password without
  any UnicodeEncodeError.
  """
  user = User()

  user.set_password('Hé')

  if not isinstance(user.password, bytes):
    # when actually retrieved from database, it should be unicode
    user.password = str(user.password)

  assert user.authenticate('Hé')
