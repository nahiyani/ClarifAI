from transformers import BartTokenizer, BartForConditionalGeneration
import math

tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text, max_input_length=1024, min_summary_ratio=0.1, max_summary_ratio=0.2):
    tokens = tokenizer.encode(text, return_tensors="pt", truncation=False)[0]
    input_token_len = len(tokens)

    chunks = [tokens[i:i + max_input_length] for i in range(0, input_token_len, max_input_length)]

    summaries = []
    for chunk in chunks:
        input_ids = chunk.unsqueeze(0)

        input_len = chunk.shape[0]
        dynamic_summary_len = math.ceil(input_len * max_summary_ratio)
        min_len = math.ceil(input_len * min_summary_ratio)

        summary_ids = model.generate(
            input_ids,
            max_length=dynamic_summary_len,
            min_length=min_len,
            num_beams=6,
            length_penalty=1.0,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)

    return "\n".join(summaries)