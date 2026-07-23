from jinja2 import Environment, FileSystemLoader # type: ignore
import os
import shutil

# 1. Setup
env = Environment(loader=FileSystemLoader('templates'))
os.makedirs('dist', exist_ok=True)

# 2. Compile Templates
for file_name in os.listdir('templates'):
    if file_name != 'layout.html' and file_name.endswith('.html'):
        # Load the specific child template
        template = env.get_template(file_name)
        # Render it (Jinja automatically follows the {% extends %} tag inside the file)
        output = template.render(page_id=file_name)
        # Save it to the dist folder
        with open(f"dist/{file_name}", "w") as f:
            f.write(output)
        print(f"Created dist/{file_name}")

# 3. Copy Static Assets Folder
if os.path.exists('static'):
    # This deletes the old static folder in dist and replaces it with the fresh one
    shutil.copytree('static', 'dist/static', dirs_exist_ok=True)
    print("Copied static assets folder")

# 4. Copy Root Files (CNAME, robots.txt, sitemap.xml)
root_files_to_copy = ['CNAME', 'robots.txt', 'sitemap.xml']
for root_file in root_files_to_copy:
    if os.path.exists(root_file):
        shutil.copy2(root_file, f"dist/{root_file}")
        print(f"Copied root file: {root_file}")
