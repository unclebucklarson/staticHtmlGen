import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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

class TestLeafNode(unittest.TestCase):
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode('a', "this would be a link")
        self.assertEqual(node.to_html(), "<a>this would be a link</a>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "zoinks scooby")
        self.assertEqual(node.to_html(), "zoinks scooby")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode('p', None)
        with self.assertRaises(ValueError):
            node.to_html()

class TestParent(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
if __name__ == "__main__":
    unittest.main()
