from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Chatbot:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def responder(self, pergunta):
        inputs = self.tokenizer.encode(pergunta + self.tokenizer.eos_token, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=200, pad_token_id=self.tokenizer.eos_token_id)
        resposta = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return resposta