from __future__ import unicode_literals

from re_scan import Scanner


scanner = Scanner([
    ('bold',         r'\*\*'),
    ('link_special', r'\[\[(?P<target>.*?)\|(?P<text>.*?)\]\]'),
    ('link',         r'\[\[(.*?)\]\]'),
    ('underline',    r'_'),
])

input_text = 'Hello **World**! [[Stuff|extra]] _[[Stuff]]_.'

for token, match in scanner.scan_with_holes(input_text):
    if token is None:
        print('hole', match)
    else:
        print('token', (token, match.groups(),
                        match.groupdict(), match.group()))
