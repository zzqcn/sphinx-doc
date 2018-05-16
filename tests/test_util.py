# -*- coding: utf-8 -*-
"""
    test_util
    ~~~~~~~~~~~~~~~

    Tests util functions.

    :copyright: Copyright 2007-2017 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import pytest

from sphinx.util import (
    encode_uri, parselinenos, split_docinfo
)


def test_encode_uri():
    expected = (u'https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_'
                u'%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_'
                u'%D0%B1%D0%B0%D0%B7%D0%B0%D0%BC%D0%B8_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85')
    uri = (u'https://ru.wikipedia.org/wiki'
           u'/Система_управления_базами_данных')
    assert expected, encode_uri(uri)

    expected = (u'https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+is%3A'
                u'sprint-friendly+user%3Ajupyter&type=Issues&ref=searchresults')
    uri = (u'https://github.com/search?utf8=✓&q=is%3Aissue+is%3Aopen+is%3A'
           u'sprint-friendly+user%3Ajupyter&type=Issues&ref=searchresults')
    assert expected, encode_uri(uri)


def test_splitdocinfo():
    source = "Hello world.\n"
    docinfo, content = split_docinfo(source)
    assert docinfo == ''
    assert content == 'Hello world.\n'

    source = ":orphan:\n\nHello world.\n"
    docinfo, content = split_docinfo(source)
    assert docinfo == ':orphan:\n'
    assert content == '\nHello world.\n'

    source = ":author: Georg Brandl\n:title: Manual of Sphinx\n\nHello world.\n"
    docinfo, content = split_docinfo(source)
    assert docinfo == ':author: Georg Brandl\n:title: Manual of Sphinx\n'
    assert content == '\nHello world.\n'

    source = ":multiline: one\n\ttwo\n\tthree\n\nHello world.\n"
    docinfo, content = split_docinfo(source)
    assert docinfo == ":multiline: one\n\ttwo\n\tthree\n"
    assert content == '\nHello world.\n'


def test_parselinenos():
    assert parselinenos('1,2,3', 10) == [0, 1, 2]
    assert parselinenos('4, 5, 6', 10) == [3, 4, 5]
    assert parselinenos('-4', 10) == [0, 1, 2, 3]
    assert parselinenos('7-9', 10) == [6, 7, 8]
    assert parselinenos('7-', 10) == [6, 7, 8, 9]
    assert parselinenos('1,7-', 10) == [0, 6, 7, 8, 9]
    with pytest.raises(ValueError):
        parselinenos('1-2-3', 10)
    with pytest.raises(ValueError):
        parselinenos('abc-def', 10)
    with pytest.raises(ValueError):
        parselinenos('-', 10)