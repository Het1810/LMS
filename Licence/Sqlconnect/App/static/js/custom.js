//function confirmDelete(clientId, clientName) {
//    var confirmDelete = confirm("Are you sure you want to delete " + clientName + "?");
//    if (confirmDelete) {
//        clientDelete(clientId);
//    }
//}

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
           $(".modal-body").empty();
           $(".modal-header").empty();
           var modalFooter = $(".modal-footer");

            if (data.success) {
                // Handle success, e.g., update the table or UI
                // Append success message to the modal body
                $(".modal-header").append("<h5>Success message</h5>");
                $(".modal-body").append("<p>Data deleted successfully!</p>");

                modalFooter.find(".btn-secondary").hide();

                var okButton = $("<button>").addClass("btn btn-primary").text("OK");
                $("#yesButton").replaceWith(okButton);

                 // Remove previous click event handler
                $("#logoutModal").off("click", ".btn-primary");

                // Reattach click event to the "Yes" button
                $("#logoutModal").on("click", ".btn-primary", function () {
                    // Call the clientDelete function with the client ID
                    location.reload();
                });
                // Optionally, you can refresh the page or update UI as needed
                // location.reload();
            } else {
                // Handle failure
                // Append failure message to the modal body
                $(".modal-body").append("<p>Failed to delete data.</p>");
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            // Handle AJAX error
            // Append error message to the modal body
            $(".modal-body").append("<p>AJAX Error: " + textStatus + "</p>");
        }
    });
}

//function Deleteconfirm(clientId, clientKey) {
//
//    var confirmDelete = confirm("Are you sure you want to delete " + clientKey + "?");
//    if (confirmDelete) {
//        licenceDelete(clientId);
//    }
//}

function licenceDelete(clientId){
    var csrftoken = getCookie('csrftoken');
    var deleteUrl = '/client/licence/delete/' + clientId + '/';
    $.ajax({
        type: 'POST',
        url: deleteUrl,
        data: {},
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(data) {
           $(".modal-body").empty();
           $(".modal-header").empty();
           var modalFooter = $(".modal-footer");

            if (data.success) {
                // Handle success, e.g., update the table or UI
                // Append success message to the modal body
                $(".modal-header").append("<h5>Success message</h5>");
                $(".modal-body").append("<p>Data deleted successfully!</p>");

                modalFooter.find(".btn-secondary").hide();

                var okButton = $("<button>").addClass("btn btn-primary").text("OK");
                $("#yesButton").replaceWith(okButton);

                 // Remove previous click event handler
                $("#logoutModal").off("click", ".btn-primary");

                // Reattach click event to the "Yes" button
                $("#logoutModal").on("click", ".btn-primary", function () {
                    // Call the clientDelete function with the client ID
                    location.reload();
                });
                // Optionally, you can refresh the page or update UI as needed
                // location.reload()
            } else {
            // Handle failure
                $(".modal-body").append("<p>AJAX Error: " + textStatus + "</p>");
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            // Handle AJAX error
            $(".modal-body").append("<p>AJAX Error: " + textStatus + "</p>");
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

