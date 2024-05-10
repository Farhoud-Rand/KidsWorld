$(document).ready(function() {
    $('#register-form').submit(function(event) {
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
                    // Form submitted successfully, redirect to profile page
                    window.location.href = '/profile';
                } else {
                    // Handle unexpected response
                    console.error('Unexpected response:', response);
                }
            },
            error: function(xhr, errmsg, err) {
                // Handle error response (validation errors, etc.)
                if (xhr.status === 400) {
                    var errors = xhr.responseJSON;
                    if (errors) {
                        // Display errors in form
                        $.each(errors, function(field, fieldErrors) {
                            $('#id_' + field).addClass('is-invalid'); // Add is-invalid class to field
                            $('#id_' + field).parent().append('<div class="invalid-feedback">' + fieldErrors.join('<br>') + '</div>'); // Display error messages
                        });
                    } else {
                        // Handle unexpected error
                        console.error('Unexpected error:', errmsg, err);
                    }
                } else {
                    // Handle other HTTP errors
                    console.error('HTTP Error:', xhr.status, xhr.statusText);
                }
            }
        });
    });
});
