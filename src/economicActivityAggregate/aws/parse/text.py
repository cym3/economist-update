def textParser(textExtractResponse: dict):
  blocks = textExtractResponse["Blocks"]

  texts = []

  for block in blocks:
    if block["BlockType"] == "LINE":
      text = block["Text"].strip()
      texts.append(text)

  return texts