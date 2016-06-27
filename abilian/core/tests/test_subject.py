# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from six import text_type

from abilian.core.models.subjects import User


def test_non_ascii_password():
    """Ensure we can store and test non-ascii password without
    any UnicodeEncodeError.
    """
    user = User()

    user.set_password('Hé')

    assert isinstance(user.password, unicode)
    assert user.authenticate('Hé')
