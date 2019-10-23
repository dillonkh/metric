$(document).ready(function() {
    var name = $("#name")
    var numClasses = $("#numClasses")
    var numImages = $("#numImages")
    var url = $("#url")

    $("#but_upload").click(function() { 
        var fd = new FormData(); 
        var files = $('#file')[0].files[0]; 
        fd.append('file', files); 

        $.ajax({ 
            url: '/uploader', 
            type: 'post', 
            data: fd, 
            contentType: false, 
            processData: false, 
            success: function(response){ 
                if(response != 0){ 
                //    name.html(response["name"]) 
                //    numClasses.html(response["numClasses"]) 
                //    numImages.html(response["numImages"]) 
                //    url.html(response["url"]) 
                    alert(response)
                } 
                else{ 
                    alert('file not uploaded'); 
                } 
            }, 
        }); 
    }); 

    
    
});