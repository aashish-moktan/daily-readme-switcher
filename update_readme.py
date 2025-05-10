import datetime
import shutil

# Get current weekday name in Lowercase
day = datetime.datetime.utcnow().strftime('%A').lower()
source_file = f'readmes/{day}.md'
destination_file = 'README.md'

shutil.copyfile(source_file, destination_file)
print(f"Copied {source_file} to {destination_file}")