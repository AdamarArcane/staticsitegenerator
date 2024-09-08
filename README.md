# Static Site Generator

## Overview
A simple Static Site Generator that converts Markdown files into HTML using a customizable template. Supports recursive page generation based on the content directory structure.

## Features
- Converts Markdown to HTML
- Customizable HTML templates
- Recursive generation for multi-page sites

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/static-site-generator.git
   cd static-site-generator
   ```
   
## Usage

The primary function is `generate_pages_recursively`, which reads from the `content` directory, applies the HTML template, and saves the generated files into the `public` directory.

### Example
```python
generate_pages_recursively("content", "template.html", "public")
```
This command will:
* Recursively search the content folder for Markdown files.
* Use template.html for the layout.
* Save the generated HTML files in the public folder, preserving the structure of the content folder.

### Start the Website Locally

1. Run the site with the base or custom content:
```bash
./main.sh
```
2. View the site at: http://localhost:8888

### Function: `generate_pages_recursively`
```python
def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    """
    Generate HTML pages recursively from a content directory.

    Parameters:
    - dir_path_content: The directory containing Markdown files.
    - template_path: The path to the HTML template file.
    - dest_dir_path: The directory where the generated HTML files should be saved.

    Each Markdown file in the dir_path_content will have an equivalent HTML file in dest_dir_path.
    """
```

### Example File Structure
```
project/
│
├── content/
│   ├── index.md
│   └── blog/
│       └── post.md
│
├── public/
│   ├── index.html
│   └── blog/
│       └── post.html
│
├── template.html
│
└── main.sh
```

### Template Example
Your HTML template can include placeholders like `{{ Title }}` and `{{ Content }}`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ Title }}</title>
</head>
<body>
    <div>{{ Content }}</div>
</body>
</html>
```

### Markdown Example
Here’s an example Markdown file:
```markdown
# Welcome to My Site

This is a paragraph in Markdown.

* Item 1
* Item 2
```
The corresponding HTML will be generated in the `public` directory.

## Contribution
Feel free to fork this repository and submit pull requests for improvements or bug fixes. This project was developed for a course, but any contributions or suggestions are welcome.

