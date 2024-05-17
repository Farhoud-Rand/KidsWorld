$(document).ready(function() {
    // Get the form element
    const form = document.getElementById('profileForm');

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        // Prevent default form submission
        event.preventDefault();

        // Get the CSRF token from the hidden input field
        const csrfToken = document.getElementById('csrf_token').value;

        // Submit the form via AJAX
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
            headers: {
                'X-CSRFToken': csrfToken
            }
        })
        .then(response => {
            // Handle response status
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Handle response data
            if (data.success) {
                // Registration successful
                Swal.fire({
                    icon: 'success',
                    title: 'Success!',
                    text: 'You have successfully updated your profile.',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'OK'
                }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = '/profile';  // Redirect to profile page
                    }
                });
            } else {
                // Registration failed due to validation errors
                let errors = '';
                for (const field in data.errors) {
                    errors += `${field}: ${data.errors[field]}<br>`;
                }
                Swal.fire({
                    icon: 'error',
                    title: 'Update Profile Failed',
                    html: errors.trim(),
                    confirmButtonColor: '#d33',
                    confirmButtonText: 'OK'
                });
            }
        })
        .catch(error => {
            // Handle errors
            console.error('Error:', error);
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Something went wrong! Please try again later.',
                confirmButtonColor: '#d33',
                confirmButtonText: 'OK'
            });
        });
    });
});