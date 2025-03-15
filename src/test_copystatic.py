import unittest
from copystatic import extract_title

class TestCopyStatic(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)
"""
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")

    def test_extract_title_without_title(self):
        md = """
![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.


> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)
"""
        with self.assertRaises(Exception) as context:
            extract_title(md)
        
        self.assertEqual(str(context.exception), "No title found in the Markdown content.")

    def test_extract_title_with_title_in_the_middle(self):
        md = """
![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

# Tolkien Fan Club

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien


## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)
"""
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")       

if __name__ == "__main__":
    unittest.main()