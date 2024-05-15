$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        // Clear existing errors
        $('.is-invalid').removeClass('is-invalid');
        $('.invalid-feedback').remove();

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(), // Serialize form data
            success: function(response) {
                if (response.success) {
                    // Redirect to profile page after successful login
                    window.location.href = '/home';
                } else {
                    // Display error message from server
                    $('.messages').html('<div class="alert alert-danger alert-dismissible fade show" role="alert">Invalid username or password.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>');
                }
            },
            error: function(xhr, errmsg, err) {
                console.error('Unexpected error:', errmsg, err);
                if (xhr.status === 400) {
                    // Display error message from server for invalid credentials
                    $('.messages').html('<div class="alert alert-danger alert-dismissible fade show" role="alert">Invalid username or password.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>');
                } else {
                    // Display generic error message for other errors
                    $('.messages').html('<div class="alert alert-danger alert-dismissible fade show" role="alert">An unexpected error occurred. Please try again later.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>');
                }
            }
        });
    });
});
