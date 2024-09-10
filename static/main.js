// const form = document.getElementById('movie-form');
//     // form.onsubmit = async (e) => {
//     //     e.preventDefault();
//     //     const formData = new FormData(form);
//     //     const response = await fetch('/recommend', {
//     //         method: 'POST',
//     //         body: formData
//     //     });
//     form.onsubmit = async (e) => {
//         e.preventDefault();
//         const formData = new FormData(form);
//         const response = await fetch('/recommend', {
//             method: 'POST',
//             body: formData
//         });
//         const data = await response.json();

//         const recommendationsDiv = document.getElementById('recommendations');
//         recommendationsDiv.innerHTML = '';

//         if (data.error) {
//             recommendationsDiv.innerHTML = `<p>${data.error}</p>`;
//         } else {
//             data.titles.forEach((title, index) => {
//                 const movieDiv = document.createElement('div');
//                 movieDiv.innerHTML = `<h3>${title}</h3><img src="${data.posters[index]}" alt="${title} poster">`;
//                 recommendationsDiv.appendChild(movieDiv);
//             });
//         }
//     };

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('movie-form');

    if (form) {
        form.onsubmit = async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            try {
                const response = await fetch('/recommend', {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();

                const recommendationsDiv = document.getElementById('recommendations');
                recommendationsDiv.innerHTML = '';

                if (data.error) {
                    recommendationsDiv.innerHTML = `<p>${data.error}</p>`;
                } else {
                    data.titles.forEach((title, index) => {
                        const movieDiv = document.createElement('div');
                        movieDiv.innerHTML = `<h3>${title}</h3><img src="${data.posters[index]}" alt="${title} poster">`;
                        recommendationsDiv.appendChild(movieDiv);
                    });
                }
            } catch (error) {
                console.error('Error:', error);
                const recommendationsDiv = document.getElementById('recommendations');
                recommendationsDiv.innerHTML = `<p>There was an error processing your request. Please try again later.</p>`;
            }
        };
    } else {
        console.error("Form element not found");
    }
});
