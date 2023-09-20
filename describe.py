from transformers import BlipProcessor, BlipForConditionalGeneration
from replit.ai.modelfarm import CompletionModel


def describe_images(images):
  processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
  model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")

  descriptions = []

  for image in images:
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    descriptions.append(processor.decode(out[0], skip_special_tokens=True))

  model = CompletionModel("text-bison")
  response = model.complete(
    ["Summarize the description of this video" + "".join(descriptions)],
    temperature=0.2)

  result = response.responses[0].choices[0].content

  print("Description: ", result)
  return result
