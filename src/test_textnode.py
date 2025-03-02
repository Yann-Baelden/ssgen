import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("this is a text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_link(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text exemple", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()