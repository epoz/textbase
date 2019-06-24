from collections import OrderedDict

import textbase

example = bytes("""# Here is a comment
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
""", 'utf-8')


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


example_multiline = bytes("""
ID seg_entry_0000001
TYPE entry
TITLE Athens (in museum). Titulum antiquissimum editum a Studniczka, Ath. Mitt.
ENTRYTYPE new reading
HEADING Titulum antiquissimum editum a Studniczka, Ath. Mitt.
LABEL 1-1
VOL 1
ENTRY 1
BIBL seg_bibl_100001
INDEX seg_index_0071817
; seg_index_0090033
; seg_index_0090034
; seg_index_0090035
; seg_index_0090036
; seg_index_0090037
; seg_index_0090038
TEXT # Titulum antiquissimum editum a Studniczka 
; 
; Titulum antiquissimum editum a Studniczka, _Ath. Mitt._ XVIII, 225, denuo tractaverunt W. Brandenstein et E. Kalinka, _Klio_ XVII, 262 sq., 267 sq. — Kalinka ipse Athenis titulum in vase inscriptum examinavit atque testatur post verba ὃς νῦν ὀρχηστῶν πάντων ἀταλώτατα παίζει· non scriptum esse τοῦτο δεκᾶν μιν sed τοῦτον ἐκαύμιν, litteram autem paenultimam potius ε quam ι esse. Verba vertit: „qui nunc omnium saltatorum optime saltavit. eius amore incensus sum.” — Etiam W. Brandenstein inde profectus est ut litteram δ post τοῦτο non recte lectam esse putaret, verum pro δεκᾶν legendum esse ἑκᾶν i. e.: „dieses Gefäsz soll ihn erfreuen,” quod minime nobis persuasit. — Contra utrumque Studniczka lectionem suam defendit _Arch. Αnz._ XXXVI, 341 sq.
$
LOC a. 7, n. 5, p. [33]
URL.WEBPAGE http://opac.unimi.it/SebinaOpac/Opac?action=search&thNomeDocumento=USM1327958T
PARENT 001RAV0258734
CREATOR Heine, Thomas Theodor
ID.INV USM1327958
CAPTION.EN In and around the building of a ruined factory grow trees, shrubs and climbing plants. A woman and some poorly dressed children in ragged clothes gather flowers and grass in the meadows that grew up around the factory. At the bottom of the vignette, the following quote appears from the newspaper bulletin: &quot;Lange ist die deutsche Industrie, leblos erstarrt, im Winterschlaf darnieder gelegen&quot; Von den ersten Strahlen der Lenzsonne geküszt, beginnt sie nun aufs neue zu blühen und zu grünen &quot; , which states that the German industry has been hibernating for a long time, but that now, at the first sun of spring, it begins to bloom again and be reborn.
ANNOT Il nome dell'autore compare anche in forma di monogramma all'interno dell'immagine
; In calce alla vignetta citazione da un giornale.
TITLE.IT Frühling
IIHIM MILAN
CAPTION.IT All'interno e intorno all'edificio di una fabbrica in rovina crescono alberi, cespugli e piante rampicanti. Una donna e alcuni bambini vestiti in modo povero, con gli abiti stracciati, raccolgono fiori ed erba nei prati cresciuti intorno alla fabbrica. In calce alla vignetta compare la seguente citazione dal bollettino di borsa di un giornale: "Lange ist die deutsche Industrie, leblos erstarrt, im Winterschlaf darnieder gelegen. Von den ersten Strahlen der Lenzsonne geküszt, beginnt sie nun aufs neue zu blühen und zu grünen", in cui si afferma che l'industria tedesca è stata in letargo per lungo tempo, ma che ora, al primo sole della primavera, inizia a rifiorire e rinascere.
IC 61D(GERMANIA)
; 23D42
; 47B0
; 54F13
URL.IMAGE IIHIM_514800768.jpg
TYPE images from periodicals
URL.IMAGE.CACHED http://opac.unimi.it/sebina/repository/opac/link/0473(19020000)005_001.jpg
ID IIHIM_MILAN_-560014375
$
""", 'utf-8')


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

    output = [x for x in textbase.TextBase(example_multiline)]
    assert output == expected


if __name__ == "__main__":
    test_main()
    test_multiline()
