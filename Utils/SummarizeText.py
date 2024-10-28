from openai import OpenAI
import os 

class SummarizeText:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.modelId = "gpt-4o-mini"

    def summarize(self, text):
        completion = self.client.chat.completions.create(
            model=self.modelId,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Write a summary for given text : {text}"
                }
            ]
        )

        return completion.choices[0].message