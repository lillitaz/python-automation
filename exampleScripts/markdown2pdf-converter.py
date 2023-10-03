import sys
import markdown
from weasyprint import HTML

# Take the filename as an argument
filename = sys.argv[1]

# Read the Markdown file
input_file = open(filename, 'r')
text = input_file.read()

# Convert the Markdown to HTML
html = markdown.markdown(text)

# Create an HTML file
html_file = open(filename.replace('.md', '.html'), 'w')
html_file.write(html)
html_file.close()

# Convert the HTML file to PDF using WeasyPrint
HTML(string=html).write_pdf(filename.replace('.md', '.pdf'))

# Close the input file
input_file.close()
