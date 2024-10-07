# prompt: i need a program that takes a <iframe> using a input  and adds it to a existing gallery.html and then pushes it to GitHub that can be run locale

#@title Input your iframe code
iframe_code = input('<iframe width="640" height="360" src="https://www.youtube.com/embed/w5ebcowAJD8" title="How do QR codes work? (I built one myself to find out)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>') #@param {type:"string"}


import os
import subprocess

def update_gallery_html(iframe_code):
  """Updates the gallery.html file with the provided iframe code."""

  gallery_html_path = "gallery.html"  # Path to your gallery.html file

  try:
    with open(gallery_html_path, "r") as f:
      html_content = f.read()

    # Find the insertion point (e.g., a specific div)
    insertion_point = "</body>"

    # Insert the iframe code before the insertion point
    new_html_content = html_content.replace(insertion_point, f"{iframe_code}\n{insertion_point}")

    with open(gallery_html_path, "w") as f:
      f.write(new_html_content)

    print(f"Successfully updated {gallery_html_path} with the iframe code.")

  except FileNotFoundError:
    print(f"Error: {gallery_html_path} not found.")
    return False
  except Exception as e:
    print(f"An error occurred: {e}")
    return False

  return True


def git_push_changes():
  """Stages, commits, and pushes changes to GitHub."""

  try:
    # Stage the changes
    subprocess.run(["git", "add", "."], check=True)

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "Update gallery with new iframe"], check=True)

    # Push the changes
    subprocess.run(["git", "push"], check=True)

    print("Successfully pushed changes to GitHub.")

  except subprocess.CalledProcessError as e:
    print(f"Git command failed: {e}")
    return False
  except Exception as e:
    print(f"An error occurred: {e}")
    return False

  return True



if iframe_code:
  if update_gallery_html(iframe_code):
    print("Iframe code added to gallery.html.")
    # Uncomment the following lines if you want to automatically push changes to GitHub:

    # if git_push_changes():
    #   print("Gallery changes pushed to GitHub.")
    # else:
    #   print("Failed to push gallery changes to GitHub.")

else:
  print("Please enter the iframe code.")

git_push_changes()