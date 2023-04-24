import unittest
from pypdf import PdfReader


class TestPdfReader(unittest.TestCase):
    def test_pdf_reader(self):
        reader = PdfReader("data/Attention Is All You Need.pdf")
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            self.assertIsNotNone(text)


if __name__ == "__main__":
     unittest.main()
