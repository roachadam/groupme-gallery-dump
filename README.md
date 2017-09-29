# groupme-gallery-dump
Dumps all images from a GroupMe chat.

# Work Required
In order for this script to work, you need to dump the html from the chat you wish to retrieve images from.
Steps:
1. Go to https://web.groupme.com and select the chat you want.
2. Click the chat title and select 'Gallery' from the drop down.
3. Continue pressing 'Load More' until you load all images.
4. Inspect the html of the gallery dialog, and save the entire html.

# Usage
groupme-gallery-dump.py dump.html myFolder
