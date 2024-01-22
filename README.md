# ATS-Resume-Analyzer

<p align="center">
  <img src=resume_icon.jpg width="500px" height="500px" >
  <br>
  <em>Image obtained from <a href="https://ideogram.ai">ideogram.ai</a></em>
</p>

## Overview

This is an ATS Resume Analyzer using the Gemini Pro model through Vertex AI and the magic of prompt engineering. You can follow these steps to analyze your own resume.

1. Copy-Paste a Job description in the provided box (Use Command+Enter or Ctrl+Enter)
2. Upload your Resume in PDF format
3. Use the different buttons to analyze your resume.

## Buttons

- "Tell me about your Resume" will provide a overview of how well you match by mentioning your strengths and weaknesses.

- "Percentage match" will show you how well your resume match the JD.

- "Project Ideas" will suggest you two portfolio projects to include in your resume that can increase your percentage match. And Finally

- "Resume Re-Structure Suggestions" will provide you different ways to make your resume better in terms of the structure, writing style, etc.

## Demo

This is how the streamlit app looks like:

<p align="center">
  <img src=streamlit_homepage.png width="700px" height="400px" >
</p>

**Disclaimer**
This product is only for educational purposes and not for commercial use.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

## How to use

1. Clone this repository

```bash
git clone https://github.com/bhargobdeka/ATS-Resume-Analyzer.git
```

2. change to the folder

```bash
cd ATS-Resume-Analyzer
```

3. open a virtual environment in VScode

```bash
python3.10 -m venv .venv
```

4. install all the modules from requirements.txt

```bash
pip install -r requirements.txt
```

5. You need to have a Google Cloud account. Go to [Google Cloud Console](https://console.cloud.google.com/welcome?project=ats-gemini-project) and open a project. Also need to enable Vertex AI API for use in Canada. Then in the terminal initialize your project using

```bash
gcloud init
```

and follow the corresponding steps (if required).

6. Then initialize vertex AI using your own project intead of mine, i.e., 'ats-gemini-project' in line 4 of app.py

```bash
vertexai.init(project='ats-gemini-project')
```

7. The last step is to run app.py using

```bash
streamlit run app.py
```

## Acknowledgement

I would like to extend my heartfelt thanks to [Krish Naik](https://www.youtube.com/@krishnaik06) for his end-to-end tutorials on GenAI. In my code, I used the 'gemini pro' model instead of the 'gemini-pro-vision' to read directly from uploaded PDF.

## Collaboration

Let me know if someone wants to build GenAI apps with me. Always open to cool projects and cool people!
