// static/script.js
// Minimal JS for column highlight
document.querySelectorAll('.comparison-table td').forEach(cell => {
    cell.addEventListener('mouseover', () => {
        const colIndex = Array.from(cell.parentElement.children).indexOf(cell);
        document.querySelectorAll(`.comparison-table tr td:nth-child(${colIndex + 1}), .comparison-table tr th:nth-child(${colIndex + 1})`).forEach(el => {
            el.style.backgroundColor = '#e0e0e0';
        });
    });
    cell.addEventListener('mouseout', () => {
        const colIndex = Array.from(cell.parentElement.children).indexOf(cell);
        document.querySelectorAll(`.comparison-table tr td:nth-child(${colIndex + 1}), .comparison-table tr th:nth-child(${colIndex + 1})`).forEach(el => {
            el.style.backgroundColor = '';
        });
    });
});