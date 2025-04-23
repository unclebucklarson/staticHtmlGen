import unittest

from htmlnode import HTMLNode
from htmlnode import LEAFNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        html_node_1 = HTMLNode("a", "zork", [1, 2, 3], {"href":"https://git.com", "target": "bonkers"})
        self.assertEqual(' href="https://git.com" target="bonkers"',html_node_1.props_to_html() )

    def test_repr(self):
        # print("In test_repr")
        html_node_1 = HTMLNode("a", "zork", [1, 2, 3], {"href":"https://git.com", "target": "bonkers"})
        self.assertEqual("tag: a, value: zork, children: [1, 2, 3], props: {'href': 'https://git.com', 'target': 'bonkers'}", html_node_1.__repr__())
    
    def test_to_html(self):
        # print("in test_to_html")
        html_node_1 = HTMLNode("a", "zork", [1, 2, 3], {"href":"https://git.com", "target": "bonkers"})
        
        with self.assertRaises(NotImplementedError):
            html_node_1.to_html()

class TestLEAFNode(unittest.TestCase):
    
    def test_leaf_to_html_p(self):
        node = LEAFNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LEAFNode('a', "this would be a link")
        self.assertEqual(node.to_html(), "<a>this would be a link</a>")
    
    def test_leaf_to_html_no_tag(self):
        node = LEAFNode(None, "zoinks scooby")
        self.assertEqual(node.to_html(), "zoinks scooby")
    
    def test_leaf_to_html_no_value(self):
        node = LEAFNode('p', None)
        with self.assertRaises(ValueError):
            node.to_html()
        
if __name__ == "__main__":
    unittest.main()
