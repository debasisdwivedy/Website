import unittest

from utility_block import markdown_to_blocks, markdown_to_html_node
from blocknode import BlockNode

class TestUtilityBlock(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                BlockNode("This is **bolded** paragraph"),
                BlockNode("This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line"),
                BlockNode("- This is a list\n- with items"),
            ],
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        import re
        nodes = markdown_to_html_node(md)
        html = nodes.to_html()
        # print("===============================")
        # print(text)
        # print("===============================")
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """
        nodes = markdown_to_html_node(md)
        html = nodes.to_html()
        # print(f"{str(html)}---->")
        # print(f"{html}==<div><pre><code>This is text that _should_ remain\n the **same** even with inline stuff\n</code></pre></div>" )
        # print(html ==r"<div><pre><code>This is text that _should_ remain\n the **same** even with inline stuff\n</code></pre></div>" )
        self.assertEqual(
        html,
        r"<div><pre><code>This is text that _should_ remain\n the **same** even with inline stuff\n</code></pre></div>",
    )
    
    def test_headings(self):
        md = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

This is a paragraph with a [link](https://www.google.com).

This is a image link ![alt text for image](url/of/image.jpg)

- Item 1
- Item 2
- Item 3

1. Item 1
2. Item 2
3. Item 3


> This is a quote.


"""
        nodes = markdown_to_html_node(md)
        html = nodes.to_html()
        self.assertEqual(html,
                         '<div><h1> Heading 1</h1><h2> Heading 2</h2><h3> Heading 3</h3><h4> Heading 4</h4><h5> Heading 5</h5><h6> Heading 6</h6><p>This is a paragraph with a <a href="https://www.google.com">link</a>.</p><p>This is a image link <img src="url/of/image.jpg" alt="">alt text for image</img></p><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol><blockquote> This is a quote.</blockquote></div>',
                        )