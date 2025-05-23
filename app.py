from lxml import etree

print("🏁 LXML is working!")
root = etree.Element("root")
print(etree.tostring(root, pretty_print=True).decode())
