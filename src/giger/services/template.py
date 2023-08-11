from jinja2 import Template


class TemplateService:
    def render(self, template, data):
        template = Template(template)
        return template.render(data)
