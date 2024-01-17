import textwrap
import re
wrapper = textwrap.TextWrapper(7)
dedented_text = textwrap.dedent('123 45 6')
wrapped = wrapper.fill(text=dedented_text)

def justify(text, width):
  
    prev_txt = text
    while((l:=width-len(text))>0):
        text = re.sub(r"(\s+)", r"\1 ", text, count=l)
        if (text == prev_txt): break
    return text.rjust(width)

# def justify(text, width):
#     wrapped = wrap(text, width)
#     print(wrapped)
#     for line in wrapped:
#         line = line.split()
#         spaces = " "
#         while len(line) < width:
#             line = spaces.join(line)
#             spaces += " "
            
#     return "\n".join(wrapped)

for l in wrapped.splitlines():
    print(justify(l, 7))
