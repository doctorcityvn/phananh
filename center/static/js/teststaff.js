

        function hide1() {
         $("#trangtrieuchung").hide();
        $("#trangxlkc").hide();
        $("#trangdichvu").hide();
        $("#trangdonthuoc").hide();
        $("#trangchat").hide();


        }



        $(document).ready(function(){






          $("#clicktrieuchung").click(function(){

            hide1();$("#trangtrieuchung").show();

          });

        $("#clickxlkc").click(function(){

            hide1();$("#trangxlkc").show();

          });

          $("#clickdichvu").click(function(){

            hide1();$("#trangdichvu").show();

          });
          $("#clickdonthuoc").click(function(){

            hide1();$("#trangdonthuoc").show();

          });
          $("#clickchat").click(function(){

            hide1();$("#trangchat").show();

          });




        });


