from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "ibm-granite/granite-3.3-2b-instruct"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Create pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Core generation function
def generate_text(prompt, max_length=1024):
    result = generator(prompt, max_length=max_length, do_sample=True, temperature=0.7)[0]["generated_text"]
    return result

def generate_code(prompt):
    return generate_text(prompt)

def fix_code(code):
    prompt = f"Fix the bugs in the following code:\n{code}"
    return generate_text(prompt)

def document_code(code):
    prompt = f"Generate documentation for the following code:\n{code}"
    return generate_text(prompt)
