$(document).ready(function() {

    var dat;

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
        newInput.setAttribute("type", "number");
        newInput.setAttribute("id", "layer" + index);
        newInput.setAttribute("name", "num");
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

            localStorage.setItem("dataset",lines)
            dat = lines
            // var data = JSON.stringify({ "model_type": "nn_binary_classification", "dataset": lines, "layers": 5, "neurons": 20 })
    
            // var settings = {
            //     "url": "http://127.0.0.1:5000/model/train",
            //     "method": "POST",
            //     "timeout": 0,
            //     "headers": {
            //       "x-access-token": localStorage.token,
            //       "Content-Type": "application/json"
            //     },
            //     "data": data,
            //   };
    
            //   $.ajax(settings).done(function (response) {
            //     console.log(response);
            //   });
    
        }
    
        fr.readAsText(this.files[0]);
    })
});