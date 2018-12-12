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


if __name__ == "__main__":
    test_main()
