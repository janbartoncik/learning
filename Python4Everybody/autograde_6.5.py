text = "X-DSPAM-Confidence:    0.8475"

# ws = where is
ws = text.find("0")
ws = int(ws)
print(float(text[ws:]))