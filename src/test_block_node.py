import unittest
from blocknode import BlockType, BlockNode

class Test_Block_Node(unittest.TestCase):
    def test_block_to_block_type(self):
        block1 = BlockNode("- This is a list\n- with items")
        block2 = BlockNode("# This is a heading")
        block3 = BlockNode("```\n import pytorch ```")
        block4 = BlockNode("> This is a Quote")
        block5 = BlockNode("1. This is a ordered list")
        block6 = BlockNode("Hello how are you")

        self.assertEqual(block1.block_to_block_type(),BlockType.UNORDERED_LIST)
        self.assertEqual(block2.block_to_block_type(),BlockType.HEADING)
        self.assertEqual(block3.block_to_block_type(),BlockType.CODE)
        self.assertEqual(block4.block_to_block_type(),BlockType.QUOTE)
        self.assertEqual(block5.block_to_block_type(),BlockType.ORDERED_LIST)
        self.assertEqual(block6.block_to_block_type(),BlockType.PARAGRAPH)