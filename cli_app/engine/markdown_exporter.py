from datetime import datetime
from pathlib import Path

md_file_name = datetime.now().strftime("%A_%d_%b_%Y.md").lower()
md_file_path = Path("~").expanduser().joinpath(md_file_name)


def export_markdown(title, url):
    md_content = f"""
#### {title} 
{url}
"""
    with open(md_file_path, "a+") as f:
        f.write(md_content)
