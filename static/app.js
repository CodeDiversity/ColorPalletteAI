

const form = document.querySelector('#form');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  getColors();
});

// test comment

function createColorBoxes(colors, container) {
  container.innerHTML = '';
  for (const color of colors) {
    const div = document.createElement('div');
    div.classList.add('color');
    div.style.backgroundColor = color;
    div.style.width = `calc(100% / ${colors.length})`;
    div.style.height = '100vh';
    const span = document.createElement('span');
    span.innerText = color;
    div.addEventListener('click', () => {
      navigator.clipboard.writeText(color);
    });
    div.appendChild(span);
    container.appendChild(div);
  }
}

function getColors() {
  const query = form.elements.query.value;
  fetch('/palette', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      query: query,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      const colors = data.colors;
      const container = document.querySelector('.container');
      createColorBoxes(colors, container);
    });
}
