var productPrices = {};

function calculateValue() {
    var grandTotal = 0;
    $(".product-box-extra .product-item").each(function() {
        var qty = parseFloat($(this).find(".product-qty").val()) || 0;
        var price = parseFloat($(this).find(".product-price").val()) || 0;
        var total = qty * price;
        
        // Input box value setup
        $(this).find(".product-total").val(total.toFixed(2));
        grandTotal += total;
    });
    $("#product_grand_total").val(grandTotal.toFixed(2));
}

$(function () {
    $.get('http://127.0.0.1:5000/getProducts', function (response) {
        productPrices = {};
        if(response) {
            var options = '<option value="">--Select--</option>';
            $.each(response, function(index, product) {
                options += '<option value="'+ product.product_id +'">'+ product.name +'</option>';
                productPrices[product.product_id] = product.price_per_unit;
            });
            
            $(".product-box").find("select").empty().html(options);
            
            if ($(".product-box-extra").children().length === 0) {
                var initialRow = $(".product-box").html();
                $(".product-box-extra").append(initialRow);
                
                // Form element attributes setup
                var firstRow = $(".product-box-extra .product-item").last();
                firstRow.find(".cart-product").attr("name", "product");
                firstRow.find(".product-qty").attr("name", "qty");
                firstRow.find(".product-total").attr("name", "item_total");
                
                $(".product-box-extra .remove-row").last().addClass('hideit');
            }
        }
    });
});

$("#addMoreButton").click(function () {
    var row = $(".product-box").html();
    $(".product-box-extra").append(row);
    
    var newRow = $(".product-box-extra .product-item").last();
    newRow.find(".cart-product").attr("name", "product");
    newRow.find(".product-qty").attr("name", "qty");
    newRow.find(".product-total").attr("name", "item_total");
    
    $(".product-box-extra .remove-row").last().removeClass('hideit');
    $(".product-box-extra .product-price").last().val('0.0');
    $(".product-box-extra .product-qty").last().val('1');
    $(".product-box-extra .product-total").last().val('0.0');
});

$(document).on("click", ".remove-row", function (){
    $(this).closest('.product-item').remove();
    calculateValue();
});

$(document).on("change", ".cart-product", function (){
    var product_id = $(this).val();
    var price = productPrices[product_id] || 0;

    $(this).closest('.product-item').find('.product-price').val(price);
    calculateValue();
});

// Event handling logic optimized for inputs and updates
$(document).on("input change", ".product-qty", function (e){
    calculateValue();
});

$("#saveOrder").on("click", function(){
    var formData = $("form").serializeArray();
    
    var requestPayload = {
        customer_name: null,
        grand_total: null,
        order_details: []
    };
    
    for(var i=0; i<formData.length; ++i) {
        var element = formData[i];
        var lastElement = null;

        switch(element.name) {
            case 'customerName':
                requestPayload.customer_name = element.value;
                break;
            case 'product_grand_total':
                requestPayload.grand_total = element.value;
                break;
            case 'product':
                if (element.value !== "") {
                    requestPayload.order_details.push({
                        product_id: element.value,
                        quantity: null,
                        total_price: null
                    });
                }
                break;
            case 'qty':
                lastElement = requestPayload.order_details[requestPayload.order_details.length-1];
                if(lastElement) lastElement.quantity = element.value;
                break;
            case 'item_total':
                lastElement = requestPayload.order_details[requestPayload.order_details.length-1];
                if(lastElement) lastElement.total_price = element.value;
                break;
        }
    }
    
    if(requestPayload.order_details.length === 0) {
        alert("Please select at least one valid product!");
        return;
    }
    
    $.ajax({
        url: 'http://127.0.0.1:5000/insertOrder',
        type: 'POST',
        data: { 'data': JSON.stringify(requestPayload) },
        success: function(response) {
            alert("Order Saved Successfully!");
            window.location.reload();
        },
        error: function(error) {
            alert("Error saving order. Check your terminal output logs.");
            console.log(error);
        }
    });
});