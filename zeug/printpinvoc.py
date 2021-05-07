from sys import stdin,stdout
from pathlib import Path
import logging
def slurp_pinyin():
    pinyin={}
    for fp in Path('.').glob('pin[0-9]*.tsv'):
        with open(fp) as f:
            for line in f.readlines():
                try:
                    chr,pin=line.strip().split('\t')
                    pinyin[chr]=pin
                except Exception as e:
                    logging.error(e)
                    logging.error(fp)
                    raise
    return pinyin
def main():
    pinyin=slurp_pinyin()
    for line in (_.strip() for _ in stdin.readlines()):
        try:
            word,trans_de=line.split('\t')
        except Exception as e:
            logging.error(e)
            logging.error(line)
            raise
        result=word+' ('
        chars=(_ for _ in word)
        for char in chars:
            try:
                pin=pinyin[char]
            except KeyError as e:
                # https://en.wikipedia.org/wiki/CJK_Unified_Ideographs
                if ord(char) < 0x4e00 or ord(char) == 0x8ba0:
                    pin=char
                else:
                    logging.error(e)
                    logging.error(char)
                    raise
            result+=pin
        result+=f')\t{trans_de}'
        print(result)
        
if __name__=='__main__':
    main()
