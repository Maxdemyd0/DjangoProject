document.getElementById('calcForm')!.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the default form submission

    const num1 = (document.getElementById('num1') as HTMLInputElement).value;
    const num2 = (document.getElementById('num2') as HTMLInputElement).value;
    const operation = (document.getElementById('operation') as HTMLSelectElement).value;

    // Create the URL
    const url = `/calc/${operation}/${num1}/${num2}`;

    // Redirect the user to the generated URL
    window.location.href = url; // Redirects to the new URL
});