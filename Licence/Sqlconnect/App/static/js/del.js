function Deleteconfirm(clientId) {
    var confirmDelete = confirm("Are you sure U want to delete " + clientId + "?");
    if (confirmDelete) {
        clientDelete(clientId);
    }
}

function clientDelete(clientId){
    var csrftoken = getCookie('csrftoken');
    var deleteUrl = '/client/delete/' + clientId + '/';
    $.ajax({
        type: 'POST',
        url: deleteUrl,
        data: {},
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(data) {
            if (data.success) {
            // Handle success, e.g., update the table or UI
                alert('Data deleted successfully!');
            // Refresh the page
                location.reload();
            } else {
            // Handle failure
                alert('Failed to delete data.');
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            // Handle AJAX error
            alert('AJAX Error: ' + textStatus);
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie has the specified name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}