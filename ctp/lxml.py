import lxml.etree as ET from lxml

# Read the content of a XML file
dom = ET.parse('home5tei.xml')

# Read the XSL file
xslt = ET.parse('home5.xsl')

# Build a XSL transformer
# create an instance of the class XSLT
transform = ET.XSLT(xslt)

# Perform the transformation
# the result is an instance of the class ElementTree
newdom = transform(dom)

# transform the ElementTree instance in a string and print it 
print(ET.tostring(newdom, pretty_print=True))

# write the string in a html document
with open("ex_py.html", "wb") as f:
 f.write(ET.tostring(newdom, pretty_print=True))