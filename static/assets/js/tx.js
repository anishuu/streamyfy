$(document).ready(function() {
  $('.movie-card').click(function() {
      var showId = $(this).data('show-id'); // Extract Show_id from the data attribute
      var userId = '{{ user.id }}'; // Assuming you have the User_id available in the template

      // Send AJAX request to Django
      $.ajax({
          type: 'POST',
          url: '{% url "save_watch_history" %}',
          data: {
              'show_id': showId,
              'user_id': userId,
              'csrfmiddlewaretoken': '{{ csrf_token }}'
          },
          success: function(response) {
              console.log(response);
              // Optionally, you can redirect the user to the movie page or do other actions upon successful save
          },
          error: function(xhr, errmsg, err) {
              console.log(xhr.status + ": " + xhr.responseText); // Log any errors
          }
      });
  });
});