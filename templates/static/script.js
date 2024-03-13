document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('qa-form');
    const answerDiv = document.getElementById('answer');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch('http://localhost:5000/answer', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            answerDiv.innerHTML = `<p>${data.answer}</p>`;
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
