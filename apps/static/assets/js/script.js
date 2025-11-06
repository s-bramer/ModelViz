const divider = document.querySelector('.divider');
const mapColumn = document.querySelector('.map-column');
const contentColumn = document.querySelector('.content-column');

let isResizing = false;
let startX;

divider.addEventListener('mousedown', function(e) {
    isResizing = true;
    startX = e.clientX; // Capture the initial mouse position
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
});

function onMouseMove(e) {
    if (!isResizing) return;

    const container = document.querySelector('.resizable-container');
    const containerRect = container.getBoundingClientRect();
    const offsetX = e.clientX - containerRect.left;

    const newMapWidth = offsetX - (divider.offsetWidth / 2);

    if (newMapWidth >= 100 && newMapWidth <= containerRect.width - 100) {
        mapColumn.style.width = `${newMapWidth}px`;
        contentColumn.style.width = `${containerRect.width - newMapWidth - divider.offsetWidth}px`;
    }
}

function onMouseUp() {
    isResizing = false;
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
}
