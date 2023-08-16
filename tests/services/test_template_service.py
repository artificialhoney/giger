from jinja2 import Template

from giger.services.template import TemplateService

__author__ = "Sebastian Krüger"
__copyright__ = "Sebastian Krüger"
__license__ = "MIT"


def test_render():
    """TemplateService().render"""
    template = "A {{hero}} with long hair and sword"
    data = {"hero": "viking"}
    assert TemplateService().render(template, data) == Template(template).render(data)
