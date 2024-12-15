# AI-powered Presentation Generator
Creates content for a presentation given a PDF document. Uses a crew of LLM agents build using CrewAI to achive this.

## Setup:
1. Clone the repository 
```
git clone https://github.com/akshatpandya/presentation-generator.git
```
2. Create a `.env` file similar to `example.env`. Update the `OPENAI_API_KEY` with your key. If you don't have an OpenAI API key, you can get one by signing up on OpenAI [website](https://openai.com/api/).
3. Install the dependencies 
```
pip install requirements.txt
```
4. Replace the `document.pdf` with your desired PDF file. 
5. Run the app 
```
python main.py
```
