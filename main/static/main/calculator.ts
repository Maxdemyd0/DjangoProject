document.getElementById('calcForm')!.addEventListener('submit', (event) => {
    event.preventDefault();

    const num1 = (document.getElementById('num1') as HTMLInputElement).value;
    const num2 = (document.getElementById('num2') as HTMLInputElement).value;
    const operation = (document.getElementById('operation') as HTMLSelectElement).value;

    window.location.href = `/calc/${operation}/${num1}/${num2}`;
});