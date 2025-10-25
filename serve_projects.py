from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)
PROJECTS_DIR = './projects'

def get_file_type(filename):
    ext = filename.split('.')[-1].lower()
    if ext in ['cpp', 'c', 'h']: return 'C/C++'
    elif ext in ['py']: return 'Python'
    elif ext in ['html']: return 'HTML'
    elif ext in ['css']: return 'CSS'
    elif ext in ['js']: return 'JavaScript'
    elif ext in ['md']: return 'Markdown'
    else: return 'Other'

def read_file_content(path, max_bytes=2000):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read(max_bytes)
    except:
        return ''

# JSON for single project
@app.route('/projects/<project>.json')
def project_json(project):
    folder_path = os.path.join(PROJECTS_DIR, project)
    files_list = []
    if os.path.isdir(folder_path):
        for file_name in sorted(os.listdir(folder_path)):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                files_list.append({
                    "name": file_name,
                    "type": get_file_type(file_name),
                    "code": read_file_content(file_path)
                })
    return jsonify({"name": project, "files": files_list})

# Serve raw files
@app.route('/projects/<project>/<filename>')
def serve_file(project, filename):
    return send_from_directory(os.path.join(PROJECTS_DIR, project), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
