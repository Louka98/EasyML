$(document).ready(function() {

    var dat;

    $('#model_type').change(function() {
        console.log("asdasd")
        var act_func = document.getElementById("act_func");
        var hidden_act_func = document.getElementById("hidden_act_func");
        var loss = document.getElementById("loss");
        var layers = document.getElementsByName("num");
        var last_layer = layers[layers.length-1];

        if($(this).val() == "binary")
        {
            act_func.value = "sigmoid";
            hidden_act_func.value = "relu";
            loss.value = "binary_crossentropy";
            last_layer.value = 1;
        }
        if($(this).val() == "multi_class")
        {
            act_func.value = "softmax";
            hidden_act_func.value = "relu";
            loss.value = "categorical_crossentropy";
            last_layer.value = 2;
        }
        if($(this).val() == "multi_label")
        {
            act_func.value = "sigmoid";
            hidden_act_func.value = "relu";
            loss.value = "binary_crossentropy";
            last_layer.value = 2;
        }
      });

    $('#add_layer').click(function(){
        var tbodyRef = document.getElementById('layers').getElementsByTagName('tbody')[0];

        // Insert a row at the end of table
        var newRow = tbodyRef.insertRow();

        var newCell2 = newRow.insertCell();
        var newDiv = document.createElement("div");
        newDiv.setAttribute("class", "col-sm-2 form-group")
        newDiv.innerHTML = '<i class="material-icons iconInput" style="font-size:36px">layers</i>'
        newCell2.appendChild(newDiv)

        // Insert a cell at the end of the row
        var newCell = newRow.insertCell();
        var index = document.getElementById('layers').getElementsByTagName('input').length;
        // Append a text node to the cell
        var newInput = document.createElement("INPUT");
        newInput.required = true;
        newInput.setAttribute("type", "number");
        newInput.setAttribute("id", "layer" + index);
        newInput.setAttribute("name", "num");
        newInput.setAttribute("value", "1");
        newInput.setAttribute("min", "1");
        newInput.setAttribute("class", "form-control")
        newInput.setAttribute("placeholder", "number of neurons");
        newCell.appendChild(newInput);
        window.scrollBy(0,59);
    } );

    $('#remove_layer').click(function(){
        len = document.getElementById('layers').getElementsByTagName('input').length;

        if (len > 2)
        {
            document.getElementById("layers").deleteRow(len-1);
        }
        window.scrollBy(0,-59);
    });

    $('#run').click(function(){
        //VALIDATION
        $("#error_msg").hide();
        $("#error_msg_layers").hide();

        inputfile = document.getElementById("inputfile");
        if(!inputfile.checkValidity())
        {
            $("#error_msg").show();
                document.getElementById("error_msg").innerHTML = "input file: " + inputfile.validationMessage;
                return;
        }

        var layer_inputs = document.getElementsByName("num")
        for (let inp of layer_inputs)
        {
            if (!inp.checkValidity()) {
                $("#error_msg_layers").show();
                document.getElementById("error_msg_layers").innerHTML = inp.id +" "+ inp.validationMessage;
                return;
            }
        }

        var target = document.getElementById("target");
        if(!target.checkValidity() || !dat[0].includes(target.value))
        {
            $("#error_msg").show();
            document.getElementById("error_msg").innerHTML = "Please specify a valid target colum name!";
            return; 
        }

        var categorical = document.getElementById("categorical").value;
        var cat = categorical.split(",");
        for(let e of cat)
        {
            if(!dat[0].includes(e) && cat[0] != "")
            {
                $("#error_msg").show();
                document.getElementById("error_msg").innerHTML = "Please specify a valid categorical colum name!";
                return; 
            }
        }
        
        epochs = document.getElementById("epochs");
        if(!epochs.checkValidity())
        {
            $("#error_msg").show();
                document.getElementById("error_msg").innerHTML = "epochs: " + epochs.validationMessage;
                return;
        }

        test_size = document.getElementById("test_size");
        if(!test_size.checkValidity())
        {
            $("#error_msg").show();
                document.getElementById("error_msg").innerHTML = "test size: " + test_size.validationMessage;
                return;
        }

        //END VALIDATION
        var data = [];
        var target_column = "";
        var layers = []; 
        var cat_cols = [];
        var epochs = 1;
        var test_size = 0.1;
        $('input').each(function() {
            data.push({
            "name": $(this).attr('id'),
            "value": $(this).val()
            })
            if ($(this).attr('id') == "target") {  target_column = $(this).val(); }
            if ($(this).attr('id').includes("layer")) { layers.push(parseInt($(this).val())); }
            if ($(this).attr('id') == "categorical") { cat_cols.push($(this).val()); }
            if ($(this).attr('id') == "epochs") { epochs = parseInt($(this).val()); }
            if ($(this).attr('id') == "test_size") { test_size = parseFloat($(this).val()); }
        });

        document.getElementById("model_type").value;
        var act_func = document.getElementById("act_func").value;
        var hidden_act_func = document.getElementById("hidden_act_func").value;
        var loss = document.getElementById("loss").value;
        //console.log(localStorage.dataset)

        var data = JSON.stringify({"dataset":dat,"target_column":target_column,"cat_cols":cat_cols,"labels_included":true,"model_type" : "nn_custom","layers" : layers,"act_func": act_func, "hidden_act_func": hidden_act_func, "loss" : loss, "batch_size": 10, "epochs": epochs, "early_stopping":true, "test_size": test_size})
    
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
              

              $.ajax(settings).done(function (response) {
                console.log(response);
                
                

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

                var x = document.getElementById("loader");
                document.getElementById("run").disabled = false ;
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