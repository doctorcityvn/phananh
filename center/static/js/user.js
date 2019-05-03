$(document).ready(function() {
             // executes when HTML-Document is loaded and DOM is ready


            myhide();
            $("#map").show();
            $("#manhinhchinh").show();
            $("#pre1").hide();
            $("#back1").hide();
           $("#row1").hide();






        });
function myshow12(){

     $("#trang1").show();
            $("#dvcdtnha").show();
            $("#dkcgia").show();
            $("#dvcstnha").show();
            $("#manhinhchinh").show();

}
    function myshow(){
    $("#map").show();
            $("#dvcdtnha").show();
            $("#dkcgia").show();
            $("#dvcstnha").show();
            $("#manhinhchinh").show();
}
         function myhide(){
               $("ul").hide();
             $("#pan2").hide();
            $("#pan3").hide();
            $("#timduocbacsy").hide();

            $("#pan10").hide();
            $("#panbenhsu").hide();
            $("#panthongtin").hide();
            $("#pantrieuchung").hide();
            $("#panxuly").hide();
            $("#pandichvu").hide();
            $("#pandonthuoc").hide();
            $("#panchat").hide();
            $("#pantiepnhan").hide();
            $("#pantiepnhan2").hide();

            $("#mothongtin").hide();
            $("#mobenhsu").hide();
            $("#moxuly").hide();
            $("#modichvu").hide();
            $("#mochat").hide();
            $("#motrieuchung").hide();
            $("#modonthuoc").hide();
            $("#duongke").hide();
            $("#myBtn").hide();
            $("#panttgn").hide();
            $("#mohosokham").hide();



            $("#pankbtnha").hide();
            $("#songtimbacsy").hide();
            $("#pandongychonbacsy").hide();
            $("#dvcdtnha").hide();
            $("#dkcgia").hide();
            $("#dvcstnha").hide();
            $("#ttdvgnhat").hide();

            $("#panhoso").hide();
            $("#panlichsu").hide();
            $("#panttgn").hide();
            $("#panhoso").hide();

            $("#map").hide();
            $("#manhinhchinh").hide();
            $("#doibacsy").hide();


            document.getElementById("mySidenav").style.width = "0";

        }

        $(document).ready(function(){


            $("#tiep9").click(function(){
                if ($(kbtnha).is(":visible")) {

                    myhide();
                    $("#row1").show();

                    $("#pankbtnha").show();
                    $("#map").show();
                     return;
                }
                if ($(datdichvu).is(":visible")) {

                    myhide();
                    $("#map").show();
                    $("#songtimbacsy").show();
                    $("#songtimbacsy").delay(2000).fadeOut(0);
                    $("#timduocbacsy").delay(2000).fadeIn(0);
                    $("#pankbtnha").hide();
                     return;
                }

                if ($(timduocbacsy).is(":visible")) {

                    myhide();
                    $("#map").show();
                    $("#doibacsy").show();
                    $("#timduocbacsy").hide();
                     return;
                }


            });
            $("#qualai9").click(function(){
                if ($(kbtnha).is(":visible")) {
                    location.href = 'https://doctorcityvn.pythonanywhere.com/menu/';
                     return;

                }

                if ($(datdichvu).is(":visible")) {
                    myhide();
                    myshow();
                    return;
                }
                if ($(timduocbacsy).is(":visible")) {
                     myhide();
                    $("#row1").show();

                    $("#pankbtnha").show();
                    $("#map").show();

                     return;
                }
                if ($(doibacsy).is(":visible")) {

                    myhide();
                    $("#map").show();
                    $("#timduocbacsy").show();
                    $("#pankbtnha").hide();
                     return;
                }


            });




          $("#thongtin").click(function(){

            myhide();
            $("#pan1").hide();
            $("#map").hide();

            $("#myBtn").show();
            $("#mothongtin").show();
            $("#modichvu").show();
            $("#modonthuoc").show();
            $("#mohosokham").show();
            document.getElementById("mySidenav").style.width = "0";
            $("#panttgn").show();



          });

          $("#lichsu").click(function(){
             myhide();


            $("#panlichsu").show();
            document.getElementById("mySidenav").style.width = "0";

          });
          $("#kbtnha").click(function(){
              myhide();
            $("#row1").show();

            $("#pankbtnha").show();
            $("#map").show();




          });
          $("#tuchoi").click(function(){
             myhide();
             myshow();




          });

          $("#tuchoi1").click(function(){
             myhide();
             myshow();
          });
          $("#tuchoidoibacsy").click(function(){
             myhide();
             myshow();
          });


        $("#huykbtnha").click(function(){
              $("#panchat").hide();$("#panthongtin").hide();$("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();
              $("#songtimbacsy").hide();
              $("#map").hide();


            $("#pankbtnha").show();


          });

        $("#myBtn").click(function(){
            myhide();$("#map").show(); $("#trang1").show();
            $("#dvcdtnha").show();
            $("#dkcgia").show();
            $("#dvcstnha").show();
            $("#manhinhchinh").show();



          });
          $("#hoanthienhoso").click(function(){
            $("ul").hide();
            $("#pan2").show();
            $("#pan1").hide();
            $("#myBtn").show();

          });
          $("#mohosokham").click(function(){
            $("ul").hide();
            $("#pan3").show();
            $("#pan31").show();
            $("#pan2").hide();
            $("#pan1").hide();
            $("#mothongtin").show();
            $("#mobenhsu").show();
            $("#moxuly").show();
            $("#modichvu").show();
            $("#mochat").show();
            $("#motrieuchung").show();
            $("#modonthuoc").show();
            $("#panthongtin").show();
            $("#duongke").show();$("#myBtn").show();



          });


          $("#mothongtin").click(function(){
            $("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();

            $("#panttgn").show();
            $("#panhoso").hide();

          });

          $("#mobenhsu").click(function(){
              $("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();

            $("#panbenhsu").show();

          });
          $("#motrieuchung").click(function(){
              $("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();

            $("#pantrieuchung").show();

          });
          $("#moxuly").click(function(){
              $("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();

            $("#panxuly").show();

          });
          $("#modichvu").click(function(){
              $("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();

            $("#pandichvu").show();
            $("#panhoso").hide();

          });
          $("#modonthuoc").click(function(){
              $("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();

            $("#pandonthuoc").show();
            $("#panhoso").hide();

          });

          $("#mohosokham").click(function(){
              $("#panthongtin").hide();$("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();

            $("#panhoso").show();

          });





            $("#datdichvu").click(function(){
                myhide();
                $("#map").show();
                $("#songtimbacsy").show();
                $("#songtimbacsy").delay(10000).fadeOut(0);
                $("#timduocbacsy").delay(10000).fadeIn(0);





                $("#pankbtnha").hide();

          });
$("#dongychonbacsy").click(function(){

    $("#doibacsy").show();
    $("#timduocbacsy").hide();
});



        $("#myRange3").click(function(){
            var r1=document.getElementById("myRange3") ;

            if (r1.value == 2) {
                $("#panchat").hide();$("#panthongtin").hide();$("#panttgn").hide();$("#panbenhsu").hide(); $("#pantrieuchung").hide();$("#panxuly").hide();$("#pandichvu").hide();$("#pandonthuoc").hide();$("#panchat").hide();
                $("#trang1").hide();
                $("#myRange3").hide();
                $("#map").hide();
                $("#pankbtnha").show();
            }
        });

          $("#luuthongtin").click(function(){


            $("#pan1").show();
            $("#pan2").hide();

          });
        });