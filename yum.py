import subprocess
import json

def search_photos(query):
    cmd = ["node", "cum.js", query]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)