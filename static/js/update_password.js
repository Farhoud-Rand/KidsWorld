// Get the CSRF token from the hidden input field
const csrfToken = document.getElementById('csrf_token').value;
            
// Get the form element
const form = document.getElementById('passwordForm');

// Add event listener for form submission
form.addEventListener('submit', function(event) {
    // Prevent default form submission
    event.preventDefault();

    // Submit the form via AJAX
    fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: {
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => {
        console.log('Response Status:', response.status); // Debugging: Log response status
        return response.json();
    })
    .then(data => {
        console.log('Response Data:', data); // Debugging: Log response data

        if (data.success) {
            // Registration successful
            Swal.fire({
                icon: 'success',
                title: 'Success!',
                text: 'You have been successfully updated your password.',
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = '/profile';  // Redirect to home page
                }
            });
        } else {
            // Registration failed due to validation errors
            let errors = '';
            for (const field in data.errors) {
                errors += `${data.errors[field]}<br>`;
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