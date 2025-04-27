import unittest

from htmlnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from htmlnode import TextType
from htmlnode import text_node_to_html_node

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
class TetTexNode(unittest.TestCase):
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node")
        
    def test_italics(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a italic node")
    
    # code
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code node")
        
    # link
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        
    # image
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
    
if __name__ == "__main__":
    unittest.main()
