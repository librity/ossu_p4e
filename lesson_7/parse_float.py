text = "X-DSPAM-Confidence:    0.8475"

f_position = text.find(':')
number = float(text[f_position+1:])

print(number)
