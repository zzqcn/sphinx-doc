# -*- coding: utf-8 -*-
"""
    test_api_translator
    ~~~~~~~~~~~~~~~~~~~

    Test the Sphinx API for translator.

    :copyright: Copyright 2007-2017 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import sys

import pytest
from util import rootdir


def setup_module():
    sys.path.insert(0, rootdir / 'roots' / 'test-api-set-translator')


def teardown_module():
    sys.path.remove(rootdir / 'roots' / 'test-api-set-translator')


@pytest.mark.sphinx('html')
def test_html_translator(app, status, warning):
    # no set_translator(), no html_translator_class
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'SmartyPantsHTMLTranslator'


@pytest.mark.sphinx('html', confoverrides={
    'html_translator_class': 'translator.ExtHTMLTranslator'})
def test_html_with_html_translator_class(app, status, warning):
    # no set_translator(), but html_translator_class
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ExtHTMLTranslator'


@pytest.mark.sphinx('html', confoverrides={
    'html_use_smartypants': False})
def test_html_with_smartypants(app, status, warning):
    # no set_translator(), html_use_smartypants=False
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'HTMLTranslator'


@pytest.mark.sphinx('html', testroot='api-set-translator')
def test_html_with_set_translator_for_html_(app, status, warning):
    # use set_translator(), no html_translator_class
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfHTMLTranslator'


@pytest.mark.sphinx('html', testroot='api-set-translator', confoverrides={
    'html_translator_class': 'translator.ExtHTMLTranslator'})
def test_html_with_set_translator_for_html_and_html_translator_class(
        app, status, warning):
    # use set_translator() and html_translator_class.
    # set_translator() is given priority over html_translator_clas.
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfHTMLTranslator'


# this test break test_websupport.test_comments test. why?
# @pytest.mark.sphinx(
#     buildername='dirhtml',
#     srcdir=(test_roots / 'test-api-set-translator'),
# )
# def test_dirhtml_set_translator_for_dirhtml(app, status, warning):
#     translator_class = app.builder.translator_class
#     assert translator_class
#     assert translator_class.__name__ == 'ConfDirHTMLTranslator'


@pytest.mark.sphinx('singlehtml', testroot='api-set-translator')
def test_singlehtml_set_translator_for_singlehtml(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfSingleHTMLTranslator'


@pytest.mark.sphinx('pickle', testroot='api-set-translator')
def test_pickle_set_translator_for_pickle(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfPickleTranslator'


@pytest.mark.sphinx('json', testroot='api-set-translator')
def test_json_set_translator_for_json(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfJsonTranslator'


@pytest.mark.sphinx('latex', testroot='api-set-translator')
def test_html_with_set_translator_for_latex(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfLaTeXTranslator'


@pytest.mark.sphinx('man', testroot='api-set-translator')
def test_html_with_set_translator_for_man(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfManualPageTranslator'


@pytest.mark.sphinx('texinfo', testroot='api-set-translator')
def test_html_with_set_translator_for_texinfo(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfTexinfoTranslator'


@pytest.mark.sphinx('text', testroot='api-set-translator')
def test_html_with_set_translator_for_text(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfTextTranslator'


@pytest.mark.sphinx('xml', testroot='api-set-translator')
def test_html_with_set_translator_for_xml(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfXMLTranslator'


@pytest.mark.sphinx('pseudoxml', testroot='api-set-translator')
def test_html_with_set_translator_for_pseudoxml(app, status, warning):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfPseudoXMLTranslator'
