import argparse
from pypdf import PdfReader
from summarease.model import Model


def parse_args() -> argparse.Namespace():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", type=str, required=True, help="pdf file to be read")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    model = Model()
    
    text = " "
    reader = PdfReader(f"data/{args.data}")
    for i in range(len(reader.pages)):
            page = reader.pages[i]
            page_text = page.extract_text()
            text += page_text

    input = model.encode(text)
    output = model.decode(input)
    print(output)