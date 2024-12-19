document.getElementById('askBtn').addEventListener('click', function() {
    const website = document.getElementById('website').value;
    const query = document.getElementById('query').value;

    if (website && query) {
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `website=${encodeURIComponent(website)}&query=${encodeURIComponent(query)}`
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('answer').innerText = data.answer;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
