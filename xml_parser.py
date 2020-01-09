from lxml import etree as et

root = et.fromstring(input())

results = {'blue': 0, 'red': 0, 'green': 0}

value = 0

def value_counter(xml_tree):
    global value
    value += 1
    if xml_tree.attrib['color'] in results:
        results[xml_tree.attrib['color']] += value
    for children in xml_tree:
        value_counter(children)
    value -= 1

value_counter(root)
red = results['red'] 
green = results['green'] 
blue = results['blue']

print(f"{red} {green} {blue}")