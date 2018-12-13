from collections import OrderedDict

import textbase

example = b"""# Here is a comment
NAME John Doe
DOB 19720601
COLOURS red
; green
; mauve
STORY Once upon a time there lived a frog in a 
 far away land. He was a very sprightly frog 
 and could jump around all day long.
$
NAME Peter Piper
DOB 19840101
COLOURS black
; purple
; white
$
# ANd this is effectively an empty record.
$
"""


def test_main():
    expected = [
        {
            "NAME": ["John Doe"],
            "DOB": ["19720601"],
            "COLOURS": ["red", "green", "mauve"],
            "STORY": [
                """Once upon a time there lived a frog in a far away land. He was a very sprightly frog and could jump around all day long."""
            ],
        },
        {
            "NAME": ["Peter Piper"],
            "DOB": ["19840101"],
            "COLOURS": ["black", "purple", "white"],
        },
    ]

    output = [x for x in textbase.TextBase(example)]

    assert output == expected


def test_multiline():
    expected = [
        OrderedDict({
            "ID": ["seg_entry_0000001"],
            "TYPE": ["entry"],
            "TITLE": ["Athens (in museum). Titulum antiquissimum editum a Studniczka, Ath. Mitt."],
            "ENTRYTYPE": ["new reading"],
            "HEADING": ["Titulum antiquissimum editum a Studniczka, Ath. Mitt."],
            "LABEL": ["1-1"],
            "VOL": ["1"],
            "ENTRY": ["1"],
            "BIBL": ["seg_bibl_100001"],
            "INDEX": [
                "seg_index_0071817",
                "seg_index_0090033",
                "seg_index_0090034",
                "seg_index_0090035",
                "seg_index_0090036",
                "seg_index_0090037",
                "seg_index_0090038",
            ],
            "TEXT": [
                """# Titulum antiquissimum editum a Studniczka 

 Titulum antiquissimum editum a Studniczka, _Ath. Mitt._ XVIII, 225, denuo tractaverunt W. Brandenstein et E. Kalinka, _Klio_ XVII, 262 sq., 267 sq. — Kalinka ipse Athenis titulum in vase inscriptum examinavit atque testatur post verba ὃς νῦν ὀρχηστῶν πάντων ἀταλώτατα παίζει· non scriptum esse τοῦτο δεκᾶν μιν sed τοῦτον ἐκαύμιν, litteram autem paenultimam potius ε quam ι esse. Verba vertit: „qui nunc omnium saltatorum optime saltavit. eius amore incensus sum.” — Etiam W. Brandenstein inde profectus est ut litteram δ post τοῦτο non recte lectam esse putaret, verum pro δεκᾶν legendum esse ἑκᾶν i. e.: „dieses Gefäsz soll ihn erfreuen,” quod minime nobis persuasit. — Contra utrumque Studniczka lectionem suam defendit _Arch. Αnz._ XXXVI, 341 sq.""",
            ],
        }),
    ]

    with open("x", "rb") as f:
        output = [x for x in textbase.TextBase(f)]

    assert output == expected


if __name__ == "__main__":
    test_main()
    test_multiline()
