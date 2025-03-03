import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html_with_href(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.example.com"})
        assert node.props_to_html() == ' href="https://www.example.com"' 

    def test_props_to_html_with_no_props(self):
        node = HTMLNode(None, None, None, None)
        assert node.props_to_html() == ""

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode("div", "Content", None, {"class": "container", "id": "main"})
        result = node.props_to_html()
        assert ' class="container"' in result
        assert ' id="main"' in result
        assert result.startswith(' ')

if __name__ == "__main__":
    unittest.main()