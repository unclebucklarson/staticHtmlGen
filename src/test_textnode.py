import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    
    # def test_eq(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertEqual(node, node2)


    # def test_not_equal(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text nod2e", TextType.BOLD)
    #     self.assertNotEqual(node, node2)
    
    # def test_url_is_none(self):
    #     node = TextNode("url should be null", TextType.IMAGE)
    #     self.assertIs(node.url, None)
        
    # def test_url_is_not_none(self):
    #     node = TextNode("url is set to someting", TextType.CODE, "www.cncstuff.com")
    #     self.assertIsNotNone(node.url)
        
    # def test_texttype_is_code(self):
    #     node = TextNode("url is set to someting", TextType.CODE, "www.cncstuff.com")
    #     self.assertIs(node.text_type, TextType.CODE)
    pass
        
if __name__ == "__main__":
    unittest.main()