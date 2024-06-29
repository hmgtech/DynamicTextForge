import google.generativeai as genai
import os

genai.configure(api_key="api-key")

model = genai.GenerativeModel('gemini-1.5-flash')


prompt = """Look at the current Hero section:
{
    "section_name": "Hero",
    "content": [
        {
            "type": "headline",
            "text": "Optimize your team's holiday schedules for just $10."
        },
        {
            "type": "paragraph",
            "text": "Exclusive holiday discount for new clients: You pay only $10 now through January 1 for unlimited employees, calendars, and dashboards."
        },
        {
            "type": "LpButtonReact",
            "text": "Start Scheduling"
        }
    ]
}
It is designed for ScheduleMaster, a digital scheduler to help someone schedule tasks.
Now, replace the text with LeadPages content: LeadPages, a landing page builder to help you build landing pages for your business.
Keep format same section name, just replace the text.
Please come up with innovative ideas and attractive statements. In response, just give me best json object."""

response = model.generate_content(prompt)
print(response.text)
