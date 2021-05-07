import argparse
import sys
from dataclasses import dataclass
from lxml import etree
@dataclass
class Vocable:
    character:str
    pinyin:str
    meaning:str
def get_entry(character:str,root):
    entry=root.xpath('//card/entry/headword[. = "他们"]/..')[0]
    pronunciation=entry.xpath('child::pron')[0].text
    definition=entry.xpath('child::defn')[0].text
def normalize_text(txt: str):
    return txt.replace("\u200c", "").replace("\u2011", "-")


def parse_cli_args():
    argpar = argparse.ArgumentParser()
    argpar.add_argument("--input", default=sys.stdin, type=argparse.FileType("r"))
    argpar.add_argument("--type", choices=["voc","pin"], type=str)

    argpar.add_argument("--pin", type=argparse.FileType("r"))
    argpar.add_argument("--voc", type=argparse.FileType("r"))
    argpar.add_argument("--rad", type=argparse.FileType("r"))

    argpar.add_argument("--output", default=sys.stdout, type=argparse.FileType("w"))
    argpar.add_argument("--field-separator", default="\t", type=str)
    return argpar.parse_args()
def make_markdown():
    pass
        

def main():
    args = parse_cli_args()
    txt=normalize_text(args.voc.read())
    for line in txt.splitlines():
        character=line.split('\t')[0]
        args.output.write(f"{character}\n")

if __name__ == "__main__":
    raise NotImplementedError("TODO: Finish module")
