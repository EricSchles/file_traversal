# We have a few thousand `.md` files that are missing one line of front-matter data, and the only place that we have the data _(as a string)_ is in the filename itself `2013-07-02-example-slug.md`.

# If we can access the filename, we can use regex to add the proper `url:` format in the front matter.
# Do you know if there is a way we can access the filename as a variable in a find and replace?


# The files in the /content/posts/ folder are what need to be modified.
# https://github.com/GSA/digitalgov.gov/tree/demo/content/posts
# The root of the repo is here: https://github.com/GSA/digitalgov.gov

# You can either download the repo, modify just the files in the /content/posts/, or you can check out the repo, make the changes an push them up in a new branch.


# Filename: `2013-07-02-example-slug.md`

# Current Front Matter
#---
# date: 2013-07-02 11:08:48 -0400
# title: 'Fueleconomy.gov &#8211; Usability Case Study'
# summary: 'Summary goes here...'
# authors:
#   - jonathan-rubin
# categories:
#   - user-testing-and-research
# tag:
#   - user experience
# ---

# Desired Front Matter
# ---
# url: 2013/07/02/example-slug
# date: 2013-07-02 11:08:48 -0400
# title: 'Fueleconomy.gov &#8211; Usability Case Study'
# summary: 'Summary goes here...'
# authors:
#   - jonathan-rubin
# categories:
#   - user-testing-and-research
# tag:
#   - user experience
# ---


# - - - - - - - - - - - - - - - - - -
# Possible Fix
# Python:

import os


def parse_file(file_path):

    file_name = file_path.split("/")[-1]
    parts = file_name.split('-', 3)
    url = '/'.join(parts)
    with open(file_path) as f:
        contents = f.read()
    if url not in contents:
        with open(file_path, 'w') as f:
            # write out the contents with a new second line
            contents = "\n".join(contents.split("\n")[1:])
            f.write('---\n')
            f.write('url: ')
            f.write(url +'\n')
            f.write(contents)

for root, dirs, files in os.walk(os.getcwd()):        
    for index, File in enumerate(files):
        if not File.endswith(".py"):
            full_path = os.path.join(root, File)
            print("at file", full_path)
            parse_file(full_path)
    
