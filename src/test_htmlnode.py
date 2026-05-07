import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_none_props_returns_empty_string(self):
        node = HTMLNode(None, None, None, None)
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_empty_props_returns_empty_string(self):
        node = HTMLNode(None, None, None, {})
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_one_prop_returns_one_string(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com"')

    def test_multiple_props(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, World!", None)
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')
