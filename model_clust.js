$(document).ready(function() {

    var dat;

    $('#model_type').change(function() {
        // var act_func = document.getElementById("act_func");
        // var hidden_act_func = document.getElementById("hidden_act_func");
        // var loss = document.getElementById("loss");
        // var layers = document.getElementsByName("num");
        // var last_layer = layers[layers.length-1];

        // if($(this).val() == "binary")
        // {
        //     act_func.value = "sigmoid";
        //     hidden_act_func.value = "relu";
        //     loss.value = "binary_crossentropy";
        //     last_layer.value = 1;
        // }
        // if($(this).val() == "multi_class")
        // {
        //     act_func.value = "softmax";
        //     hidden_act_func.value = "relu";
        //     loss.value = "categorical_crossentropy";
        //     last_layer.value = 2;
        // }
        // if($(this).val() == "multi_label")
        // {
        //     act_func.value = "sigmoid";
        //     hidden_act_func.value = "relu";
        //     loss.value = "binary_crossentropy";
        //     last_layer.value = 2;
        // }
      });


    $('#run').click(function(){
        //VALIDATION
        $("#error_msg").hide();

        inputfile = document.getElementById("inputfile");
        if(!inputfile.checkValidity())
        {
            $("#error_msg").show();
                document.getElementById("error_msg").innerHTML = "input file: " + inputfile.validationMessage;
                return;
        }


        var clust = document.getElementById("clusters");
        if(!clust.checkValidity())
        {
            $("#error_msg").show();
            document.getElementById("error_msg").innerHTML = clust.validationMessage;
            return; 
        }
        
        var categorical = document.getElementById("categorical").value;
        var cat = categorical.split(",");
        console.log(cat)
        for(let e of cat)
        {
            if(!dat[0].includes(e) && cat[0] != "")
            {
                $("#error_msg").show();
                document.getElementById("error_msg").innerHTML = "Please specify a valid categorical colum name!";
                return; 
            }
        }
        
        //END VALIDATION
        var cat_cols = [];
        $('input').each(function() {
            if ($(this).attr('id') == "categorical") { cat_cols.push($(this).val()); }
        });

        var model_type = document.getElementById("model_type").value;

        var data = JSON.stringify({"dataset":dat,"target_column":"","cat_cols":cat_cols,"labels_included":true,"model_type" : model_type,"n_clusters": parseInt(clust.value)})
    
        var x = document.getElementById("loader");
        document.getElementById("run").disabled = true;
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }

            var settings = {
                "url": "http://127.0.0.1:5000/model/train",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "x-access-token": localStorage.token,
                  "Content-Type": "application/json"
                },
                "data": data,
              };
    
              $.ajax(settings, function (response) {

              }).done(function(response){
                console.log(response);

                var div = document.getElementById("result_div");
                div.setAttribute("style","height:1000px");
                var div2 = document.getElementById("result_div2");
                div2.setAttribute("style","height:1200px");

                var canvas = document.getElementById("result_canvas"); 
                canvas.width  = response["width"];
                canvas.height = response["height"];
                canvas.style.zIndex   = 8;
                canvas.style.position = "absolute";
                canvas.style.border   = "1px solid";

                var ctx = canvas.getContext("2d");
                var r,g,b; 

                for(var i=0; i< response["image"].length; i++){ 
                    for(var j=0; j< response["image"][0].length; j++){ 
                        r = response["image"][i][j][0]; 
                        g = response["image"][i][j][1];	 
                        b = response["image"][i][j][2];		 
                        ctx.fillStyle = "rgba("+r+","+g+","+b+", 1)";  
                        ctx.fillRect( j, i, 1, 1 ); 
                    } 
                }  

                var canvas = document.getElementById("result_canvas2"); 
                canvas.width  = response["width2"];
                canvas.height = response["height2"];
                canvas.style.zIndex   = 8;
                canvas.style.position = "absolute";
                canvas.style.border   = "1px solid";

                var ctx = canvas.getContext("2d");
                var r,g,b; 

                for(var i=0; i< response["image2"].length; i++){ 
                    for(var j=0; j< response["image2"][0].length; j++){ 
                        r = response["image2"][i][j][0]; 
                        g = response["image2"][i][j][1];	 
                        b = response["image2"][i][j][2];		 
                        ctx.fillStyle = "rgba("+r+","+g+","+b+", 1)";  
                        ctx.fillRect( j, i, 1, 1 ); 
                    } 
                }
              }).fail(function(response){
                $("#error_msg").show();
                document.getElementById("error_msg").innerHTML = "Invalid input file";
              }).always(function(response){
                    var x = document.getElementById("loader");
                    document.getElementById("run").disabled = false;
                    if (x.style.display === "none") {
                        x.style.display = "block";
                    } else {
                        x.style.display = "none";
                    }
              });
        // $('#result').text(JSON.stringify(data)) 
        //return false;
    } );

    //------------------------------------------------------------------------------------------------------------------

    document.getElementById('inputfile').addEventListener('change', function () {

        var fr = new FileReader();
        fr.onload = function () {
            // document.getElementById('output')
            //     .textContent = fr.result;
            var lines = fr.result.replace(/\r\n/g, "\n").split("\n")
    
            for (let index = 0; index < lines.length; index++) {
                lines[index] = lines[index].split(",")
            }
            dat = lines;
    
        }
    
        fr.readAsText(this.files[0]);
    })
});