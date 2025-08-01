// Add an event listener for the form submission
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const priceFilter = document.getElementById('price-filter');
    const logoutButton = document.getElementById('logout-button');
    const message = document.getElementById('message');
    const urlParams = new URLSearchParams(window.location.search);
    const placeId = getPlaceIdFromURL();

    if (logoutButton) {
        logoutButton.addEventListener('click', () => {
            document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
            window.location.reload();
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email')
            const password = document.getElementById('password')

            if (email.value === '' || password.value === '') {
              message.textContent = 'Invalid Data'
            } else {
              const succes = await loginUser(email.value, password.value);
              if (succes) {
                email.value = '';
                password.value = '';
              }
            }
        });
    }
    if (priceFilter) {
        priceFilter.addEventListener('change', () => {
            const selValue = priceFilter.value;
            const placeCards = document.querySelectorAll('.place-card');

            placeCards.forEach(card => {
                const price = parseFloat(card.getAttribute('data-price'));

                if (selValue === 'All' || price <= parseFloat(selValue)) {
                    card.style.display = 'block';
                }
                else {
                    card.style.display = 'none';
                }
            });
        });
    }
    if (placeId) {
        const token = getCookie('token');
        fetchPlaceDetails(placeId, token);
    }

    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const reviewText = document.getElementById('review-text').value.trim();
            const rating = document.getElementById('rating').value;
            const token = getCookie('token');

            if (!reviewText || !rating) {
                alert('Please provide both review text and rating.');
                return;
            }

            try {
                const response = await fetch(`http://127.0.0.1:5000/api/v1/reviews`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({
                        place_id: placeId,
                        text: reviewText,
                        rating: parseInt(rating)
                    })
                });
                if (!response.ok) {
                    const contentType = response.headers.get('content-type');
        
                    if (contentType && contentType.includes('application/json')) {
                        const err = await response.json();
                        throw new Error(err.message || 'Failed to submit review.');
                    } else {
                        const errText = await response.text(); // ← ici tu récupères la vraie réponse
                        console.log('HTML error response from server:', errText); // ← à inspecter dans la console navigateur
                        throw new Error('Unexpected response from server (not JSON).');
                    }
                }

                alert('Review submitted successfully!');
                window.location.href = `place?id=${placeId}`;
            } catch (error) {
                console.error('Error submitting review:', error);
                alert(error.message);
            }
        });
    }
    checkAuthentication(placeId);
});

// Make the AJAX request to the API
async function loginUser(email, password) {
    const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });
    if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/`;
    window.location.href = 'index';
    } else {
        alert('Login failed: ' + (data.message || 'Unknown error'));
    }
}

// Check user authentication:
function checkAuthentication(placeId) {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    const logoutButton = document.getElementById('logout-button');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
        if (loginLink) loginLink.style.display = 'block';
        if (logoutButton) logoutButton.style.display = 'none';
        if (addReviewSection) addReviewSection.style.display = 'none';
        fetchPlaces();
    } else {
        if (loginLink) loginLink.style.display = 'none';
        if (logoutButton) logoutButton.style.display = 'block';
        if (addReviewSection) addReviewSection.style.display = 'block';
        if (placeId) {
            fetchPlaceDetails(placeId, token);
        }
        fetchPlaces(token);
    }
}

function getCookie(name) {
    let search = name + '=';
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca =decodedCookie.split(';');

    for(let i = 0; i < ca.length; i++) {
        let c = ca[i];

        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(search) == 0) {
            return c.substring(search.length, c.length);
        }
    }
    return "";
}

// Fetch places data:
async function fetchPlaces(token) {
    try {
        let head = {};
        if (token) {
            head.Authorization = `Bearer ${token}`;
        }

        const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
            headers: head
        });

        const json = await response.json();
        displayPlaces(json);
        
    } catch (error) {
        console.error('Error:', error);
    }
}
// Populate places list
function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;

    placesList.innerHTML = '';

    const token = getCookie('token');

    places.forEach(place => {
        const placeDiv = document.createElement('div');
        placeDiv.classList.add('place-card');
        placeDiv.setAttribute('data-price', place.price);

        let html = `
            <h2>${place.title}</h2>
            <p>${place.description}</p>
            <p>${place.location}</p>
            <p>Price per Night: ${place.price}</p>
        `;
        html += `<button class="view-details-btn" data-id="${place.id}">View Details</button>`;
        placeDiv.innerHTML = html;
        placesList.appendChild(placeDiv);
    });
    const detailButtons = document.querySelectorAll('.view-details-btn');
    detailButtons.forEach(button => {
        button.addEventListener('click', () => {
            const placeId = button.getAttribute('data-id');
            window.location.href = `place?id=${placeId}`;
        });
    });

}

async function fetchPlaceDetails(placeId, token) {
    try {
        const headers = {};
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            method: 'GET',
            headers: headers
        });

        if (!response.ok) {
            throw new Error('Failed to fetch place details');
        }

        const data = await response.json();
        displayPlaceDetails(data);

    } catch (error) {
        console.error('Error loading place:', error);
    }
}

function displayPlaceDetails(place) {
    const section = document.querySelector('#place-details .place-info');
    const reviewContainer = document.querySelector('.review-card');
    if (!section) return;

    // Vider le contenu précédent
    section.innerHTML = '';
    if (reviewContainer) reviewContainer.innerHTML = '';

    // Titre
    const title = document.createElement('h2');
    title.textContent = place.title;
    section.appendChild(title);

    // Description
    const description = document.createElement('p');
    description.textContent = place.description;
    section.appendChild(description);

    // Location
    const location = document.createElement('p');
    location.textContent = `Location: lat ${place.latitude}, long ${place.longitude}`;
    section.appendChild(location);

    // Price
    const price = document.createElement('p');
    price.textContent = `Price: ${place.price}`;
    section.appendChild(price);

    // --- Amenities ---
    if (place.amenities && place.amenities.length > 0) {
        const amenitiesTitle = document.createElement('h3');
        amenitiesTitle.textContent = 'Amenities';
        section.appendChild(amenitiesTitle);

        const amenityList = document.createElement('ul');
        place.amenities.forEach(amenity => {
            const item = document.createElement('li');
            item.textContent = amenity.name;
            amenityList.appendChild(item);
        });
        section.appendChild(amenityList);
    }

    // --- Reviews ---
    if (place.reviews && place.reviews.length > 0 && reviewContainer) {
        displayReviews(place.reviews, reviewContainer);
    }
}

function displayReviews(reviews, container) {
    let html = '';

    reviews.forEach(review => {
        html += `
        <div class="single-review">
            <p><strong>${review.user.user_first_name} ${review.user.user_last_name}</strong> says:</p>
            <p>${review.text}</p>
            <p>Rating: ${review.rating} / 5</p>
        </div>
        `;
    });

    container.innerHTML = html;
}
