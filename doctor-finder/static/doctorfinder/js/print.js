$(document).ready(function(){
          
    $("#print1").on('click',function(){
        console.log("in the script");
        printData("example4");
    });
    $("#print2").on('click',function(){
        console.log("in the script");
        printData("example1");
    });
  
  
  });
function printData(res)
{
var divToPrint=document.getElementById(res);
newWin= window.open("");
var htmlToPrint = '' +
    '<style type="text/css">' +
    'table th, table td {' +
    'border:1px solid #000;' +
    'padding;0.5em;' +
    '}' +
    '</style>';
htmlToPrint += divToPrint.outerHTML;
newWin.document.write(htmlToPrint);
newWin.print();
newWin.close();	
}



