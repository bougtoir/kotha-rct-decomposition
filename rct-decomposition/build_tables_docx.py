#!/usr/bin/env python3
"""Extract all tables from the CCT manuscript docx into a separate editable docx."""
from docx import Document


def build(src_docx='KOTHA_Framework_CCT.docx', out_docx='KOTHA_Framework_CCT_tables.docx'):
    src = Document(src_docx)
    dst = Document()
    for t in src.tables:
        nt = dst.add_table(rows=len(t.rows), cols=len(t.columns))
        nt.style = 'Table Grid'
        for i, row in enumerate(t.rows):
            for j, cell in enumerate(row.cells):
                nt.rows[i].cells[j].text = cell.text
    dst.save(out_docx)
    print(f'Saved {out_docx}')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', default='KOTHA_Framework_CCT.docx')
    parser.add_argument('--out', default='KOTHA_Framework_CCT_tables.docx')
    args = parser.parse_args()
    build(args.src, args.out)
