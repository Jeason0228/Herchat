var send_check = function(url){
    var request = new XMLHttpRequest();
    request.open(
        'GET',
        url,
        true
    );
    
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
    request.onload  = function() {
        var jsonResponse = request.response;
        return jsonResponse
     };
    request.send()
}

