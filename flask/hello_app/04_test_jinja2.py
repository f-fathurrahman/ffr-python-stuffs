from jinja2 import Template

t = Template("{{ my_list[0] }}--{{ my_list[1] }}--{{ my_list[2] }}")
print( t.render(my_list=[1.2, 3.1, "This is my list"]) )

t = Template("{{ my_dict['foo'] }}")
print( t.render( my_dict={"foo":"bar", "fooo": "baaar"} ) )

t = Template("{{ my_dict[\"fooo\"] }}")
print( t.render( my_dict={"foo":"bar", "fooo": "baaar"} ) )

# alternative
t = Template("{{ my_dict.fooo }}")
print( t.render( my_dict={"foo":"bar", "fooo": "baaar"} ) )
