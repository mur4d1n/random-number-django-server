$( document ).ready(function() {
           function show()
                {
                    $.ajax({
                        url: '/',
                        cache: false,
                        success: function(html){
                            $("#random-number").html(html);
                        }
                    });
                }

                $(document).ready(function(){
                    show();
                });
        });