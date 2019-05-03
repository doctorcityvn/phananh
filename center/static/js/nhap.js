var x1="{{ ttt }}";
var x2="{{ txlkc }}";
var x3="{{ tdv }}";
var x4="{{ tdt }}";
var x5="{{ tk }}";


        function hide1() {
         $("#trangtrieuchung").hide();
        $("#trangxlkc").hide();
        $("#trangdichvu").hide();
        $("#trangdonthuoc").hide();
        $("#trangchat").hide();
        $("#trangkhoa").hide();


        }



    $(document).ready(function() {


       document.getElementById("mySidenav").style.width = "0";
       hide1()

    });


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

            hide1();$("#trangkhoa").show();

          });




        });


