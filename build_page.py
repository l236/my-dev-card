def main():
    # Config personal information
    personal_info = {
        "name": "LI KANGJIA",
        "title": "AI Engineer",
        "description": "AI Engineer passionate about MLOPs and automation.",
        "skills": ["Python", "TensorFlow", "Git", "CI/CD", "Docker"],
        "projects": [
            {
                "name": "project1",
                "url": ""
            }
        ],
        "contact": {
            "github": "",
            "linkedin": ""
        }
    }

    # HTML template
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{personal_info['name']} - Tech Card</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
                background-color: #f4f4f4;
            }}
            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #333;
                text-align: center;
                margin-bottom: 10px;
            }}
            .title {{
                text-align: center;
                color: #666;
                font-size: 1.2em;
                margin-bottom: 20px;
            }}
            .skilss {{
                background: #007bff;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9em;
            }}
            .projects, .contact {{
                margin: 20px 0;
            }}
            a {{
                color: #007bff;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{personal_info['name']}</h1>
            <div class="title">{personal_info['title']}</div>
            <p>{personal_info['description']}</p>
            <h2>skills</h2>
            <div class="skills">
    """

    # Add skill labels
    for skill in personal_info["skills"]:
        html_content += f'                <span class="skill">{skill}</span>\n'
    
    html_content += """
        </div>

        <h2>project experiences</h2>
        <div class="projects">
            <ul>
    """

    # Add project links
    for project in personal_info['projects']:
        html_content += f' <li><a href="{project["url"]}" target="_blank">{project["name"]}</a></li>\n'
        html_content += f"""
                        </ul>
                    </div>

                    <h2>contact ways</h2>
                    <div class="contact">
                        <p>
                            <a href="{personal_info['contact']['github']}" target="_blank">GitHub</a> |
                            <a href="{personal_info['contact']['linkedin']}" target="_blank">LinkedIn</a>
                        </p>
                    </div>
                </div>
            </body>
            </html>
        """

        # Write to file
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print("index.html generated successfully!")

if __name__ == "__main__":
    main()