import webbrowser
import os

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>About Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
        }
        h1, h2 {
            text-align: center;
            color: #333;
        }
        img {
            display: block;
            margin: 0 auto;
            border-radius: 10px;
        }
        ul {
            list-style-type: square;
        }
        .info {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>About Me</h1>
        <img src="avatar.jpeg" alt="none" width="200">
        <h2>Full Name: Temirlan Ilik</h2>
        <p><strong>Age:</strong> 19</p>
        <p><strong>Brief Information:</strong> Passionate Python developer specializing in backend development and data analysis. Experienced in leading projects and teams, with a strong track record of delivering impactful solutions. Active contributor to the tech community as a speaker and organizer. Honored for his problem-solving skills as a participant in a national-level Informatics Olympiad.</p>
        <p><strong>Email:</strong> <a href="mailto:temirlan@example.com">temirlanilik76@gmail.com</a></p>
        <p><strong>Birth Country:</strong> Kazakhstan</p>
        <p><strong>Hobbies:</strong> Painting, crafting and coding.</p>
        <p><strong>Study Interests:</strong> Machine learning, mathematics, and design.</p>
        <p><strong>Languages:</strong></p>
        <ul>
            <li>Kazakh</li>
            <li>Russian</li>
            <li>English</li>
        </ul>
        <p><strong>Programming/IT Skills:</strong></p>
        <ul>
            <li>Python (Backend development, FastAPI, Flask, Django)</li>
            <li>HTML, CSS, and JavaScript</li>
            <li>Kotlin for mobile development</li>
            <li>C++ for algorithm development</li>
        </ul>
    </div>
</body>
</html>
"""

file_name = "AboutMe.html"

with open(file_name, "w", encoding="utf-8") as file:
    file.write(html_content)

file_path = os.path.abspath(file_name)

try:
    browser = webbrowser.get("macosx")
    browser.open_new_tab(f"file://{file_path}")
except webbrowser.Error:
    print("Unexpected error")
