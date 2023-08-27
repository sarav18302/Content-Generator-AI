import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from flask import Flask,request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
print("Loading ...")
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_best_beam(model, tokenizer, prompt, max_length=700, num_beams=5, temperature=0.2):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    beam_outputs = model.generate(
        input_ids,
        max_length=max_length + len(input_ids[0]),  # Account for the length of the input
        num_beams=num_beams,
        temperature=temperature,
        no_repeat_ngram_size=2,
        early_stopping=True,
        num_return_sequences=1
    )
    
    generated_text = tokenizer.decode(beam_outputs[0], skip_special_tokens=True)
    return generated_text


@app.route('/',methods=['GET'])
def result():
    
    prompt="Im a boy from little town"
    generated_text = generate_best_beam(model, tokenizer, prompt)
    return jsonify({"predict":generated_text }) 
if __name__ == "__main__":
    app.run()