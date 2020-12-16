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
                break;
            case "binary":
                break;
            case "multiLabel":
                break;
            case "DNN":
                break;
            case "DT":
                break;
            case "kNN":

                break;

            case "RF":

                break;
            case "V":

                break;
            case "supportVectorMachine":

                break;
            default:
                alert('test');
                break;
        }
    });

});

