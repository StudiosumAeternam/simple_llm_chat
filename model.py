from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
TOKENIZER_NAME = os.getenv("TOKENIZER_NAME")

tokenizer = GPT2Tokenizer.from_pretrained(TOKENIZER_NAME)
model = GPTNeoForCausalLM.from_pretrained(MODEL_NAME)

# Check if a GPU is available and if not, use a CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Move the model to the device
model = model.to(device)

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    gen_tokens = model.generate(input_ids, do_sample=True, temperature=0.9, max_length=1000).to(device)
    gen_text = tokenizer.decode(gen_tokens[:, input_ids.shape[-1]:][0], skip_special_tokens=True).to(device)
    return gen_text
