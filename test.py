example = '''# Here is a comment
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
'''

output = [ {'NAME':['John Doe'],
            'DOB':['19720601'], 'COLOURS':['red','green','mauve'],
            'STORY': ['''Once upon a time there lived a frog in a far away land. He was a very sprightly frog and could jump around all day long.''']},
           {'NAME':['Peter Piper'],
            'DOB':['19840101'], 'COLOURS':['black','purple','white'] }
         ]
import textbase

if __name__ == '__main__':
    t = textbase.TextBase(example)
    tmp = []
    for x in t:
        tmp.append(x)
    assert tmp == output
