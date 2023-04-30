from transformers import AutoTokenizer, BartForConditionalGeneration


class Model():
    def __init__(self):
        self.model =  BartForConditionalGeneration.from_pretrained("models/facebook-bart-large-cnn/")
        self.tokenizer = AutoTokenizer.from_pretrained("models/facebook-bart-large-cnn/")

    def encode(self, text):
        input = self.tokenizer([text], max_length=1024, return_tensors="pt")
        out = self.model.generate(input["input_ids"], num_beams=2, min_length=5, max_length=100)
        return out
    
    def decode(self, input):
        out = self.tokenizer.batch_decode(input, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        return out
    
    def summarise(self, text):
        model_output = self.encode(text)
        text_output = self.decode(model_output)
        return text_output
    

if __name__ == "__main__":
    ARTICLE_TO_SUMMARIZE = (
        "PG&E stated it scheduled the blackouts in response to forecasts for high winds "
        "amid dry conditions. The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were "
        "scheduled to be affected by the shutoffs which were expected to last through at least midday tomorrow."
    )
    model = Model()
    x = model.encode(ARTICLE_TO_SUMMARIZE)
    y = model.decode(x)
    print(y)
    print(type(ARTICLE_TO_SUMMARIZE))
