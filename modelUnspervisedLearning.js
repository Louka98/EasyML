$(document).ready(function () {

    $("#algorithm").change(function () {
        switch ($('#algorithm').val()) {
            case "AC":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\"> <div class=' mb-3 form-group'> " +
                    "<p class='label'>number of clusters </p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> " +
                    "<p class='label'>linkage</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> " +
                    "</div>  </span>").insertAfter("#algorithmGroup");
                break;
            case "DBSCAN":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\"> <div class=' mb-3 form-group'> " +
                    "<p class='label'>Epsilon</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> " +
                    "<p class='label'>Minimum samples</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> " +
                    "</div>  </span>").insertAfter("#algorithmGroup");
                break;
            case "KMeans":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\">" +
                    " <div class=' mb-3 form-group'> <p class='label'>number of clusters </p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " </span>").insertAfter("#algorithmGroup");
                break;
            case "M":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\">" +
                    " <div class=' mb-3 form-group'> <p class='label'>Bandwith</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " </span>").insertAfter("#algorithmGroup");
                break;
            case "SC":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\">" +
                    " <div class=' mb-3 form-group'> <p class='label'>number of clusters </p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " </span>").insertAfter("#algorithmGroup");
                break;

            default:
                alert('test');
                break;
        }
    });

});
/*


//$( "<p>Test</p>" ).insertAfter( "#algorithmGroup" );
*/
