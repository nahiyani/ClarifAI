from transformers import T5ForConditionalGeneration, T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def summarize_text(text, max_input_length=512, max_output_length=150):

    input_text = "summarize: " + text

    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=max_input_length, truncation=True)

    summary_ids = model.generate(
        input_ids,
        max_length=max_output_length,
        num_beams=4,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)