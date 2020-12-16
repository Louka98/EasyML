$(document).ready(function () {

    $("#algorithm").change(function () {
        switch ($('#algorithm').val()) {
            case "RC":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\"> <div class=' mb-3 form-group'> " +
                    "<p class='label'>alpha</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> " +
                    "</div>  </span>").insertAfter("#algorithmGroup");
                break;
            case "logisticRegression":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\">" +
                    " <div class=' mb-3 form-group'> <p class='label'>Solver </p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>Penalty</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>C</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " </span>").insertAfter("#algorithmGroup");
                break;
            case "binary":
                $("#algorithmInput").remove();
                break;
            case "multiLabel":
                $("#algorithmInput").remove();
                break;
            case "DNN":
                $("#algorithmInput").remove();
                break;
            case "DT":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\">" +
                    " <div class=' mb-3 form-group'> <p class='label'>Criterion</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>Max_depth</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " </span>").insertAfter("#algorithmGroup");
                break;
            case "kNN":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\">" +
                    " <div class=' mb-3 form-group'> <p class='label'>n_neighbours</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>Metric</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>Weights</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " </span>").insertAfter("#algorithmGroup");
                break;

            case "RF":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\">" +
                    " <div class=' mb-3 form-group'> <p class='label'>nb_estimators </p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>random_state</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " </span>").insertAfter("#algorithmGroup");
                break;
            case "V":
                $("#algorithmInput").remove();
                break;
            case "supportVectorMachine":
                $("#algorithmInput").remove();
                $("<span id=\"algorithmInput\">" +
                    " <div class=' mb-3 form-group'> <p class='label'>C</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>kernel</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>Gamma</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
                    " <div class=' mb-3 form-group'> <p class='label'>Shrinking</p> <input type='number' name='num' placeholder='' min='1' class='form-control'/> </div> " +
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
