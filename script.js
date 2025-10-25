async function loadProjects() {
  const container = document.getElementById('projects-container');
  try {
    const res = await fetch('http://localhost:5000/projects.json');
    const projects = await res.json();
    container.innerHTML = '';

    projects.forEach(project => {
      const folder = document.createElement('div');
      folder.className = 'project-folder';
      folder.innerHTML = `<h2>${project.name}</h2><div class="file-list"></div>`;
      container.appendChild(folder);

      const fileList = folder.querySelector('.file-list');

      project.files.forEach(file => {
        const f = document.createElement('div');
        f.className = 'file';
        f.innerHTML = `
          <div class="file-name">${file.name} (${file.type})</div>
          <pre class="file-code">${file.code}</pre>
        `;
        fileList.appendChild(f);

        const fileNameDiv = f.querySelector('.file-name');
        const fileCode = f.querySelector('.file-code');
        fileNameDiv.addEventListener('click', () => {
          fileCode.style.display = fileCode.style.display === 'block' ? 'none' : 'block';
        });
      });

      folder.querySelector('h2').addEventListener('click', () => {
        fileList.style.display = fileList.style.display === 'block' ? 'none' : 'block';
      });
    });

  } catch(err) {
    container.innerHTML = '<p style="color:red;">Failed to load projects.</p>';
    console.error(err);
  }
}

document.addEventListener('DOMContentLoaded', loadProjects);
