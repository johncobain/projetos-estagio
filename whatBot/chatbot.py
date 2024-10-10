from transformers import pipeline, set_seed
generator = pipeline('text-generation',device='cuda', model='gpt2-xl')
set_seed(42)

outputs = generator("Hello, I'm a language model,", max_length=60, truncation=True, num_return_sequences=5)

print(outputs[0]['generated_text'])