import webbrowser
import tempfile
import os

def open_html_in_browser(html_content):
    # Create a temporary HTML file with the desired content
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as tmp_file:
        tmp_file.write(html_content)
        # Get the path of the file
        html_path = tmp_file.name

    # Open the HTML file in the default web browser
    webbrowser.open('file://' + html_path, new=2)  # `new=2` tries to open in a new tab, if possible

    # Optional: remove the file after some time or based on some condition
    # os.unlink(html_path)  # Uncomment this line if you want to delete the file after viewing

# HTML content as a string (you can include your updated HTML here)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Domain Seized</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { font-family: Arial, sans-serif; background-color: white; color: black; padding: 20px; margin: 0; }
    .warning-box { background-color: darkred; color: white; padding: 20px; margin: 20px 0; border-radius: 5px; }
    .warning-box h1, .warning-box p { margin: 0; padding: 5px; text-align: center; }
    form { background-color: #f4f4f4; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
    label, input, select { display: block; width: 100%; margin-bottom: 10px; }
    input, select { padding: 10px; }
    .bold { font-weight: bold; }
    @media (max-width: 600px) {
        body, .warning-box { padding: 10px; }
        form { padding: 10px; }
        input[type="submit"] { width: auto; padding: 12px 20px; }
    }
</style>
</head>
<body>
<div class="warning-box">
    <h1>This Domain has been seized</h1>
    <p>Law enforcement has been monitoring messages and attachments from the ANOM platform. A number of investigations have been initiated and are ongoing.</p>
    <h1>To determine if your account is associated with an ongoing investigation, please enter any device details below:</h1>
</div>
<!-- Form and other elements go here -->
</body>
</html>
"""

# Call the function to open the HTML content in a browser
open_html_in_browser(html_content)
