from __future__ import print_function

from jinja2 import Template

x = """
<p>Uncle Scrooge nephews</p>
<ul>
{% for i in my_list %}
<li>{{ i }}</li>
{% endfor %}
</ul>
"""

template = Template(x)

print( template.render(my_list=['Huey', 'Dewey', 'Louie']) )


